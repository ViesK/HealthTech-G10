from pydantic import BaseModel
from uuid import UUID

class LocationBase(BaseModel):
    clinic_id: UUID
    name: str
    floor: str | None = None
    room_code: str | None = None
    notes: str | None = None

class LocationCreate(LocationBase):
    pass

class LocationRead(LocationBase):
    id: UUID

    class Config:
        orm_mode = True
