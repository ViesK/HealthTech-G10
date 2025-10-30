from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class ClinicSpecialty(Base):
    __tablename__ = "clinic_specialties"

    clinic_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clinics.id"),
        primary_key=True
    )
    specialty_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("specialties.id"),
        primary_key=True
    )

    clinic: Mapped["Clinic"] = relationship(
        "clinics.models.Clinic", back_populates="specialties"
    )
    specialty: Mapped["Specialty"] = relationship(
        "specialties.models.Specialty", back_populates="clinics"
    )
