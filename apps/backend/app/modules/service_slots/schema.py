from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

class AvailabilityStatus(str, Enum):
    OPEN = "OPEN"
    HELD = "HELD"
    BLOCKED = "BLOCKED"

class ServiceSlotBase(BaseModel):
    specialty_id: UUID
    clinic_id: UUID
    location_id: UUID | None = None
    start_ts: datetime
    end_ts: datetime
    capacity: int = 1
    status: AvailabilityStatus = AvailabilityStatus.OPEN
    held_until: datetime | None = None

class ServiceSlotCreate(ServiceSlotBase):
    pass

class ServiceSlotRead(ServiceSlotBase):
    id: UUID

    class Config:
        orm_mode = True
