from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String
import uuid

class Base(DeclarativeBase):
    pass

class Specialty(Base):
    __tablename__ = "specialties"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # Relaciones
    clinics: Mapped[list["ClinicSpecialty"]] = relationship(
        "clinic_specialties.models.ClinicSpecialty", back_populates="specialty"
    )

    medics: Mapped[list["MedicSpecialty"]] = relationship(
        "medic_specialties.models.MedicSpecialty", back_populates="specialty"
    )

    service_slots: Mapped[list["ServiceSlot"]] = relationship(
        "service_slots.models.ServiceSlot", back_populates="specialty"
    )
