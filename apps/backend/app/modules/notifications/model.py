from app.core.db import Base
from app.modules.users.model import UsersModel
from app.modules.appointments.model import Appointment

from datetime import datetime
from typing import List, Optional

from sqlalchemy import Integer, String, Boolean, DateTime, Numeric, JSON, func, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Notification(Base):
    __tablename__ = "notifications"

    __table_args__ = (CheckConstraint("status IN ('PENDING','SENT','FAILED')", name="ck_notifications_status")),

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    appointment_id: Mapped[int] = mapped_column(ForeignKey("appointments.id"), nullable=False)

    status: Mapped[str] = mapped_column(String(16), nullable=False, server_default="PENDING")
    subject: Mapped[Optional[str]] = mapped_column(String(200))
    template_key: Mapped[Optional[str]] = mapped_column(String)
    payload_json: Mapped[dict] = mapped_column(JSON, nullable=False, server_default="{}")
    error_message: Mapped[Optional[str]] = mapped_column(String(500))
    sent_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))