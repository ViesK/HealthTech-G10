from pydantic import BaseModel, Field
from typing import Optional

class ClinicSpecialtyBase(BaseModel):
    clinic_id: int = Field(..., gt=0)
    specialty_id: int = Field(..., gt=0)

class ClinicSpecialtyCreate(ClinicSpecialtyBase):
    pass

class ClinicSpecialtyRead(ClinicSpecialtyBase):
    id: int

class ClinicSpecialtyUpdate(BaseModel):
    clinic_id: Optional[int] = Field(None, gt=0)
    specialty_id: Optional[int] = Field(None, gt=0)
