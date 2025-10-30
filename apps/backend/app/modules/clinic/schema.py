from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal, Optional,Dict,Any
from .model import * 

class ClinicSchema(BaseModel):
    id: int = Field(..., gt=-1)
    name: str = Field(..., max_length=120)
    type: ClinicType = Field(..., description="Tipo de Clinica (Publico o Privado)")
    phone: str = Field(..., max_length=30)
    tax_id: str = Field(..., max_length=120)
    address_json: Dict[str, Any] = Field(...)
    created_at: datetime = Field(..., gt=0)
    model_config = {"from_attributes": True}

class ClinicCreate(BaseModel):
    name: str = Field(..., max_length=120)
    type: ClinicType = Field(...)
    phone: str = Field(..., max_length=30)
    tax_id: str = Field(..., max_length=120)
    address_json: Dict[str, Any] = Field(...)


class ClinicUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=120)
    type: Optional[ClinicType] = None
    phone: Optional[str] = Field(None, max_length=30)
    tax_id: Optional[str] = Field(None, max_length=120)
    address_json: Optional[Dict[str, Any]] = None
    model_config = {"from_attributes": True}