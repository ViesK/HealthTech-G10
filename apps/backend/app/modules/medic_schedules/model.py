from sqlalchemy import String, Enum, DateTime,func, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.core.db import Base
import enum
from datetime import datetime

class StatusType(enum.Enum):
    open = "open"
    held = "held"
    blocked = "blocked"


class Medic_SchedulesModel(Base):
    __tablename__ = "medic_shedules"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Claves foráneas
    medic_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinic.id"), nullable=False)

    # Horarios de trabajo
    start_ts: Mapped[datetime] = mapped_column(nullable=False)
    end_ts: Mapped[datetime] = mapped_column(nullable=False)
    
    status: Mapped[StatusType] = mapped_column(Enum(StatusType), default=StatusType.open)
    held_until: Mapped[datetime] = mapped_column(nullable=True)  # hasta cuándo está bloqueada la hora
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    medic_user = relationship("UsersModel", back_populates="schedules")
    clinic = relationship("ClinicModel", back_populates="schedules")