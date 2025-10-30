from app.core.db import Base
from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

class MedicSpecialty(Base):
    __tablename__ = "medic_specialties"
    __table_args__ = (
        UniqueConstraint("medical_user_id", "clinic_id", "specialty_id", name="uq_medic_clinic_specialty"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinic.id"), nullable=False)       # <<-- "clinic" en singular
    medical_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    specialty_id: Mapped[int] = mapped_column(ForeignKey("specialties.id"), nullable=False)

