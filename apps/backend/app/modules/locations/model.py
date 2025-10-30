from app.core.db import Base
from sqlalchemy import Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

class Location(Base):
    __tablename__ = "locations"
    __table_args__ = (
        UniqueConstraint("clinic_id", "name", name="uq_locations_clinic_name"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    floor: Mapped[str | None] = mapped_column(String(32))
    room_code: Mapped[str | None] = mapped_column(String(32))
    notes: Mapped[str | None] = mapped_column(Text())

