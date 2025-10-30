from app.core.db import Base
from datetime import datetime
from sqlalchemy import String, DateTime, func, UniqueConstraint, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Specialty(Base):
    __tablename__ = "specialties"
    __table_args__ = (
        UniqueConstraint("name", name="uq_specialties_name"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

