from app.core.db import Base
from app.modules.users.model import UsersModel
from app.modules.clinic.model import ClinicModel

from datetime import datetime
from typing import List, Optional

from sqlalchemy import Integer, String, Boolean, DateTime, Numeric, JSON, func, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Appointment(Base):
    __tablename__ = "appointments"

    __table_args__ = (
        CheckConstraint("start_ts < end_ts", name="ck_appt_time_window"),
    )
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    specialty_id: Mapped[int] = mapped_column(ForeignKey("specialties.id"), nullable=False)
    patient_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    service_slot_id: Mapped[int] = mapped_column(ForeignKey("service_slots.id"), nullable=False)
    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinic.id"), nullable=False)

    assigned_location_id: Mapped[Optional[int]] = mapped_column(ForeignKey("locations.id"))
    assigned_medic_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))

    start_ts: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_ts: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    modality: Mapped[str] = mapped_column(String(16), nullable=False, server_default="IN_PERSON")
    status: Mapped[str] = mapped_column(String(16), nullable=False, server_default="CONFIRMED")

    notes: Mapped[Optional[str]] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

