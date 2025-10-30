from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import Optional, Literal, List, Any
from datetime import datetime, date    

class AppointmentBase(BaseModel):
    specialty_id: int = Field(..., gt=0)
    patient_user_id: int = Field(..., gt=0)
    service_slot_id: int = Field(..., gt=0)
    clinic_id: int = Field(..., gt=0)

    assigned_location_id: Optional[int] = Field(None, gt=0)
    assigned_medic_id: Optional[int] = Field(None, gt=0)

    start_ts: datetime
    end_ts: datetime

    modality: Literal["IN_PERSON", "VIRTUAL"] = "IN_PERSON"
    status: Literal["CONFIRMED", "CANCELLED", "PENDING"] = "CONFIRMED"

    notes: Optional[str] = Field(None, max_length=500)

    @model_validator(mode="after")
    def _check_time_window(self):
        if self.end_ts <= self.start_ts:
            raise ValueError("end_ts debe ser posterior a start_ts")
        return self
    
class AppointmentCreate (AppointmentBase):
    pass

class AppointmentRead (AppointmentBase):
    id: int
    create_at: datetime

class AppointmentUpdate (BaseModel):
    specialty_id: Optional[int] = Field(..., gt=0)
    patient_user_id: Optional[int] = Field(..., gt=0)
    service_slot_id: Optional[int] = Field(..., gt=0)
    clinic_id: Optional[int] = Field(..., gt=0)

    assigned_location_id: Optional[int] = Field(None, gt=0)
    assigned_medic_id: Optional[int] = Field(None, gt=0)

    start_ts: Optional[datetime]
    end_ts: Optional[datetime]

    modality: Optional[Literal["IN_PERSON", "VIRTUAL"]] = "IN_PERSON"
    status: Optional[Literal["CONFIRMED", "CANCELLED", "PENDING"]] = "CONFIRMED"

    notes: Optional[str] = Field(None, max_length=500)