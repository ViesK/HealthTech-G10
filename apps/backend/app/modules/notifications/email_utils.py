# app/modules/notifications/email_utils.py
from __future__ import annotations
from datetime import datetime, timezone
from email.message import EmailMessage
from zoneinfo import ZoneInfo
from pathlib import Path
from typing import Dict, Any, Optional
import smtplib
import uuid
import urllib.parse

from jinja2 import Environment, FileSystemLoader, select_autoescape

# ====== Config rápida (ajusta a tu entorno) ======
SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USER = "95c0b0b3d319cd"
SMTP_PASS = "e16b311327e5e1"
FROM_NAME = "HealthTech"
FROM_EMAIL = "no-reply@healthTech.com"
TZ = "Europe/Madrid"

# Ruta templates Jinja
TEMPLATES_DIR = Path(__file__).resolve().parents[2] / "templates" / "notifications"
env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=select_autoescape(["html", "xml"])
)

def render_template(template_key: str, payload: Dict[str, Any]) -> tuple[str, str]:
    """Devuelve (subject, html_body) renderizados desde /templates/notifications/{template_key}/"""
    subj_tpl = env.get_template(f"{template_key}/subject.txt.j2")
    body_tpl = env.get_template(f"{template_key}/body.html.j2")
    subject = subj_tpl.render(**payload).strip()
    html_body = body_tpl.render(**payload)
    return subject, html_body

def _to_utc_z(dt_str: str) -> str:
    """Convierte ISO local/aware a formato ICS UTC Z: YYYYMMDDTHHMMSSZ"""
    dt = datetime.fromisoformat(dt_str)
    if dt.tzinfo is None:
        # Si viene naive, asumir TZ Madrid y convertir a UTC
        dt = dt.replace(tzinfo=ZoneInfo(TZ))
    return dt.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

def build_google_calendar_link(title: str, start_ts: str, end_ts: str, description: str, location: Optional[str]) -> str:
    start_z = _to_utc_z(start_ts)
    end_z = _to_utc_z(end_ts)
    params = {
        "action": "TEMPLATE",
        "text": title,
        "dates": f"{start_z}/{end_z}",
        "details": description or "",
        "ctz": TZ
    }
    if location:
        params["location"] = location
    return "https://calendar.google.com/calendar/render?" + urllib.parse.urlencode(params)

def build_ics_bytes(
    uid: str,
    title: str,
    start_ts: str,
    end_ts: str,
    description: str,
    organizer_email: str,
    attendee_email: str,
    location: Optional[str] = None
) -> bytes:
    """
    Genera un .ics sencillo (método REQUEST).
    """
    dtstart = _to_utc_z(start_ts)
    dtend = _to_utc_z(end_ts)
    loc = location or ""

    # ICS básico sin librería extra (texto plano)
    ics = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//HealthZone//Appointments//ES
METHOD:REQUEST
BEGIN:VEVENT
UID:{uid}
SUMMARY:{_escape_ics(title)}
DTSTART:{dtstart}
DTEND:{dtend}
DESCRIPTION:{_escape_ics(description)}
LOCATION:{_escape_ics(loc)}
ORGANIZER:mailto:{organizer_email}
ATTENDEE;RSVP=TRUE:mailto:{attendee_email}
END:VEVENT
END:VCALENDAR
"""
    return ics.encode("utf-8")

def _escape_ics(text: str) -> str:
    # Escapes básicos ICS
    return (text or "").replace("\\", "\\\\").replace("\n", "\\n").replace(",", "\\,").replace(";", "\\;")

def send_email_with_ics(
    to_email: str,
    subject: str,
    html_body: str,
    ics_bytes: Optional[bytes] = None
):
    msg = EmailMessage()
    msg["From"] = f"{FROM_NAME} <{FROM_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content("Tu cliente de correo no soporta HTML.")
    msg.add_alternative(html_body, subtype="html")

    if ics_bytes:
        msg.add_attachment(
            ics_bytes,
            maintype="text",
            subtype="calendar",
            filename="invite.ics",
            params={"method": "REQUEST", "name": "invite.ics"}
        )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)
