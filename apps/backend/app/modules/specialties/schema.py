from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

class SpecialtyBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=120, description="Nombre de la especialidad")

class SpecialtyCreate(SpecialtyBase):
    pass

class SpecialtyUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=120)

class SpecialtyRead(SpecialtyBase):
    id: UUID

    class Config:
        from_attributes = True
