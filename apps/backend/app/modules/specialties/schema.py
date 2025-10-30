from pydantic import BaseModel, Field
from typing import Optional


class SpecialtyBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)


class SpecialtyCreate(SpecialtyBase):
    pass


class SpecialtyRead(SpecialtyBase):
    id: int


class SpecialtyUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=120)
