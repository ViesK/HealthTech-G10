from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class MedicSpecialty(Base):
    __tablename__ = "medic_specialties"

    clinic_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clinics.id"),
        primary_key=True
    )
    medical_user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True
    )
    specialty_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("specialties.id"),
        primary_key=True
    )

    clinic: Mapped["Clinic"] = relationship(
        "clinics.models.Clinic", back_populates="medic_specialties"
    )
    medic: Mapped["User"] = relationship(
        "users.models.User", back_populates="specialties"
    )
    specialty: Mapped["Specialty"] = relationship(
        "specialties.models.Specialty", back_populates="medics"
    )
