from app.core.db import Base
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, func, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

class ServiceSlot(Base):
    __tablename__ = "service_slots"

    __table_args__ = (
        CheckConstraint("start_ts < end_ts", name="ck_slot_time_window"),
        CheckConstraint("capacity >= 1", name="ck_slot_capacity_pos"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    specialty_id: Mapped[int] = mapped_column(ForeignKey("specialties.id"), nullable=False)
    clinic_id:    Mapped[int] = mapped_column(ForeignKey("clinics.id"), nullable=False)

    start_ts: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_ts:   Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    capacity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    status:   Mapped[str] = mapped_column(String(16), nullable=False, server_default="OPEN")  # OPEN | HELD | BLOCKED
    held_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

