from pydantic import BaseModel, Field
from typing import Optional

class MedicSpecialtyBase(BaseModel):
    clinic_id: int = Field(..., gt=0)
    medical_user_id: int = Field(..., gt=0)
    specialty_id: int = Field(..., gt=0)

class MedicSpecialtyCreate(MedicSpecialtyBase):
    pass

class MedicSpecialtyRead(MedicSpecialtyBase):
    id: int
    model_config = {"from_attributes": True}

class MedicSpecialtyUpdate(BaseModel):
    clinic_id: Optional[int] = Field(None, gt=0)
    medical_user_id: Optional[int] = Field(None, gt=0)
    specialty_id: Optional[int] = Field(None, gt=0)
