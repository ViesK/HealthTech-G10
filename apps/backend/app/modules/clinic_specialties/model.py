from app.core.db import Base
from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

class ClinicSpecialty(Base):
    __tablename__ = "clinic_specialties"
    __table_args__ = (
        UniqueConstraint("clinic_id", "specialty_id", name="uq_clinic_specialty"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"), nullable=False)
    specialty_id: Mapped[int] = mapped_column(ForeignKey("specialties.id"), nullable=False)
