from pydantic import BaseModel, Field
from typing import Optional

class LocationBase(BaseModel):
    clinic_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=120)
    floor: Optional[str] = Field(None, max_length=32)
    room_code: Optional[str] = Field(None, max_length=32)
    notes: Optional[str] = Field(None, max_length=2000)

class LocationCreate(LocationBase):
    pass

class LocationRead(LocationBase):
    id: int

class LocationUpdate(BaseModel):
    clinic_id: Optional[int] = Field(None, gt=0)
    name: Optional[str] = Field(None, min_length=2, max_length=120)
    floor: Optional[str] = Field(None, max_length=32)
    room_code: Optional[str] = Field(None, max_length=32)
    notes: Optional[str] = Field(None, max_length=2000)
