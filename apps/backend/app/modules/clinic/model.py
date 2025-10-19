from sqlalchemy import String, Enum, DateTime, func, JSON
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.core.db import Base
import enum

class ClinicType(enum.Enum):
    publico = "publico"
    privado = "privado"



class ClinicModel(Base):
    __tablename__= "clinic"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    type: Mapped[ClinicType] = mapped_column()
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    tax_id: Mapped[str] = mapped_column(String(120), nullable=False)
    address_json: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    #Relacion
    schedules = relationship("Medic_SchedulesModel", back_populates="clinic")