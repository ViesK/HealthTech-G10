from datetime import datetime, timezone
from sqlalchemy.orm import Session
from .model import Notification as NotificationModel
from .schema import NotificationCreate, NotificationUpdate
from typing import Dict, Any

from .email_utils import (
    render_template, build_google_calendar_link, build_ics_bytes, send_email_with_ics
)

# Excepciones de dominio
class NotFound(Exception): ...
class SendError(Exception): ...

ORGANIZER_EMAIL = "CitasPrevias@HealthTech.com"

#_____________________Funciones Globales_____________________
def _get_or_404(db: Session, notif_id: int) -> NotificationModel:
    notif = db.get(NotificationModel, notif_id)
    if not notif:
        raise NotFound("Notification no encontrada")
    return notif

def _render_and_send(notif: NotificationModel) -> None:
    """
    Renderiza plantillas + genera link Calendar + ICS + envía email real.
    Espera que payload_json contenga las claves mínimas explicadas.
    """
    try:
        payload: Dict[str, Any] = notif.payload_json or {}

        # Datos mínimos (seguridad a prueba de fallos)
        title = payload.get("title") or f"Cita #{notif.appointment_id}"
        start_ts = payload["start_ts"]
        end_ts = payload["end_ts"]
        attendee_email = payload["attendee_email"]
        modality = payload.get("modality", "IN_PERSON")
        location = payload.get("location") if modality == "IN_PERSON" else None
        meet_url = payload.get("meet_url") if modality == "VIRTUAL" else None

        # Descripción base (aparece en .ics y en link)
        description_parts = [
            payload.get("specialty", ""),
            f"Paciente: {payload.get('patient_name','')}",
            f"Médico: {payload.get('medic_name','')}"
        ]
        if modality == "VIRTUAL" and meet_url:
            description_parts.append(f"Reunión online: {meet_url}")
        if payload.get("manage_url"):
            description_parts.append(f"Gestionar: {payload['manage_url']}")
        description = "\n".join([p for p in description_parts if p])

        # Link “Añadir a Google Calendar”
        gcal_link = build_google_calendar_link(
            title=title,
            start_ts=start_ts,
            end_ts=end_ts,
            description=description,
            location=location or meet_url
        )

        # Enriquecer payload para la plantilla HTML
        payload_enriched = {
            **payload,
            "gcal_link": gcal_link
        }

        # Render Jinja
        template_key = notif.template_key or "appointment_created"
        subject_rendered, html_body = render_template(template_key, payload_enriched)

        # UID estable (id de la notificación o de la cita) para idempotencia
        uid = f"appt-{notif.appointment_id}@tu-dominio.com"

        # ICS
        ics_bytes = build_ics_bytes(
            uid=uid,
            title=title,
            start_ts=start_ts,
            end_ts=end_ts,
            description=description,
            organizer_email=ORGANIZER_EMAIL,
            attendee_email=attendee_email,
            location=(location or meet_url)
        )

        # Enviar
        send_email_with_ics(
            to_email=attendee_email,
            subject=subject_rendered or (notif.subject or "Cita confirmada"),
            html_body=html_body,
            ics_bytes=ics_bytes
        )

        notif.status = "SENT"
        notif.sent_at = datetime.now(timezone.utc)
        notif.error_message = None
        
    except Exception as e:
        notif.status = "FAILED"
        notif.error_message = str(e)[:500]

#_____________________Funciones CRUD_____________________
def create_notification(db: Session, payload: NotificationCreate, send_now: bool = True) -> NotificationModel:
    notif = NotificationModel(**payload.model_dump())
    db.add(notif)
    db.commit()
    db.refresh(notif)

    if send_now:
        _render_and_send(notif)
        db.commit()
        db.refresh(notif)

    return notif

def read_notification(db: Session, notif_id: int) -> NotificationModel:
    return _get_or_404(db, notif_id)

def update_notification(db: Session, notif_id: int, payload: NotificationUpdate) -> NotificationModel:
    notif = _get_or_404(db, notif_id)
    data = payload.model_dump(exclude_unset=True)

    # Actualiza solo status/error_message (MVP)
    for k, v in data.items():
        setattr(notif, k, v)

    # Si pides reintento (status=PENDING), intenta enviar ahora
    if data.get("status") == "PENDING":
        _render_and_send(notif)

    db.commit()
    db.refresh(notif)
    return notif
