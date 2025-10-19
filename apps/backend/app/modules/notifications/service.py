from datetime import datetime, timezone
from sqlalchemy.orm import Session
from .model import Notification as NotificationModel
from .schema import NotificationCreate, NotificationUpdate

# Excepciones de dominio
class NotFound(Exception): ...
class SendError(Exception): ...

#_____________________Funciones Globales_____________________
def _get_or_404(db: Session, notif_id: int) -> NotificationModel:
    notif = db.get(NotificationModel, notif_id)
    if not notif:
        raise NotFound("Notification no encontrada")
    return notif

def _render_and_send(notif: NotificationModel) -> None:
    """
    MVP: simula render + envío.
    Sustituye por tu render Jinja2 y adaptador SMTP real.
    """
    try:
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
