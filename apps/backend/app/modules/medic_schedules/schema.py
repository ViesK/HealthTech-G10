from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .model import StatusType

# Para la respuesta (response)
class MedicScheduleSchema(BaseModel):
    id: int = Field(..., gt=0)
    medic_user_id: int = Field(...)
    clinic_id: int = Field(...)
    start_ts: datetime = Field(...)
    end_ts: datetime = Field(...)
    status: StatusType = Field(...)
    held_until: Optional[datetime] = None
    notes: Optional[str] = None

    model_config = {"from_attributes": True}  # para convertir automáticamente desde ORM

# Para creación
class MedicScheduleCreate(BaseModel):
    medic_user_id: int = Field(...)
    clinic_id: int = Field(...)
    start_ts: datetime = Field(...)
    end_ts: datetime = Field(...)
    status: StatusType = Field(...)
    held_until: Optional[datetime] = None
    notes: Optional[str] = None

# Para actualización parcial
class MedicScheduleUpdate(BaseModel):
    start_ts: Optional[datetime] = None
    end_ts: Optional[datetime] = None
    status: Optional[StatusType] = None
    held_until: Optional[datetime] = None
    notes: Optional[str] = None