from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

class ClinicSpecialtyBase(BaseModel):
    clinic_id: UUID = Field(..., description="UUID de la clínica asociada")
    specialty_id: UUID = Field(..., description="UUID de la especialidad asociada")

class ClinicSpecialtyCreate(ClinicSpecialtyBase):
    pass

class ClinicSpecialtyUpdate(BaseModel):
    clinic_id: Optional[UUID] = Field(None)
    specialty_id: Optional[UUID] = Field(None)

class ClinicSpecialtyRead(ClinicSpecialtyBase):
    class Config:
        from_attributes = True
