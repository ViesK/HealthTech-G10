from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

class MedicSpecialtyBase(BaseModel):
    clinic_id: UUID = Field(..., description="UUID de la clínica")
    medical_user_id: UUID = Field(..., description="UUID del médico (user_id)")
    specialty_id: UUID = Field(..., description="UUID de la especialidad")

class MedicSpecialtyCreate(MedicSpecialtyBase):
    pass

class MedicSpecialtyUpdate(BaseModel):
    clinic_id: Optional[UUID] = Field(None)
    medical_user_id: Optional[UUID] = Field(None)
    specialty_id: Optional[UUID] = Field(None)

class MedicSpecialtyRead(MedicSpecialtyBase):
    class Config:
        from_attributes = True
