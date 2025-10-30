from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal
from datetime import datetime

SlotStatus = Literal["OPEN", "HELD", "BLOCKED"]

class ServiceSlotBase(BaseModel):
    specialty_id: int = Field(..., gt=0)
    clinic_id: int = Field(..., gt=0)

    start_ts: datetime
    end_ts: datetime

    capacity: int = Field(1, ge=1)
    status: SlotStatus = "OPEN"
    held_until: Optional[datetime] = None

    @model_validator(mode="after")
    def _check_time_window(self):
        if self.end_ts <= self.start_ts:
            raise ValueError("end_ts debe ser posterior a start_ts")
        return self

class ServiceSlotCreate(ServiceSlotBase):
    pass

class ServiceSlotRead(ServiceSlotBase):
    id: int
    created_at: datetime

class ServiceSlotUpdate(BaseModel):
    specialty_id: Optional[int] = Field(None, gt=0)
    clinic_id: Optional[int] = Field(None, gt=0)

    start_ts: Optional[datetime] = None
    end_ts: Optional[datetime] = None

    capacity: Optional[int] = Field(None, ge=1)
    status: Optional[SlotStatus] = None
    held_until: Optional[datetime] = None

