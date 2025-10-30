from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import Optional, Literal, List, Any, Dict
from datetime import datetime, date   

class NotificationBase(BaseModel):
    user_id: int = Field(..., gt=0)
    appointment_id: int = Field(..., gt=0)

    status: Literal["PENDING", "SENT", "FAILED"] = "PENDING"

    subject: Optional[str] = Field(None, max_length=200)
    template_key: Optional[str] = Field(None, max_length=64)
    payload_json: Dict[str, Any] = Field(default_factory=dict)
    error_message: Optional[str] = Field(None, max_length=500)

    model_config = ConfigDict(from_attributes=True)

class NotificationCreate(NotificationBase):
    pass

class NotificationRead(NotificationBase):
    id: int
    sent_at: Optional[datetime] = None

class NotificationUpdate(BaseModel):
    status: Optional[Literal["PENDING", "SENT", "FAILED"]] = None
    error_message: Optional[str] = Field(None, max_length=500)

    model_config = ConfigDict(from_attributes=True)