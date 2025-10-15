from sqlalchemy import String, Enum, DateTime, func, Integer
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.core.db import Base

import enum

#Este model representa la tabla de la base de datos ¡REAL!

class UserType(enum.Enum):
    paciente = "paciente"
    medico = "medico"
    admin = "admin"

class UsersModel(Base):
    __tablename__ = "users"
    # El ID es el DNI del usuario
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    type: Mapped[UserType] = mapped_column(Enum(UserType), nullable=False)
    timezone: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    #Relacion
    schedules = relationship("Medic_SchedulesModel", back_populates="medic_user")