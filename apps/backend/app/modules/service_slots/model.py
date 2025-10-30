from sqlalchemy import ForeignKey, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import uuid
from datetime import datetime
from enums import AvailabilityStatus  # si tenés los enums definidos aparte

class Base(DeclarativeBase):
    pass

class ServiceSlot(Base):
    __tablename__ = "service_slots"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    specialty_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("specialties.id"), nullable=False
    )
    clinic_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("clinics.id"), nullable=False
    )
    start_ts: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    end_ts: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    status: Mapped[AvailabilityStatus] = mapped_column(
        Enum(AvailabilityStatus), nullable=False, default="OPEN"
    )
    held_until: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True))

    clinic: Mapped["Clinic"] = relationship("clinics.models.Clinic", back_populates="service_slots")
    specialty: Mapped["Specialty"] = relationship("specialties.models.Specialty", back_populates="service_slots")
