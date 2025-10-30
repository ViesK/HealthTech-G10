from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Literal, Optional
from .model import * 

#definen cómo se envían y reciben los datos entre el cliente y API

class UserSchema(BaseModel):
    id: int = Field(..., gt=0, description="DNI del usuario") #los "..." significa obligatorio, gt>0
    email: str = Field(..., max_length=120)
    full_name: str = Field(...,max_length=120)
    phone: str = Field(...,max_length=30)
    type: UserType = Field(..., description="Tipo de usuario (paciente, medico, admin)")
    timezone: str = Field(..., max_length=50)
    created_at: datetime = Field(..., gt=0)
    model_config = ConfigDict(from_attributes=True)  

class UserCreate(BaseModel):
    id: int = Field(..., gt=0, description="DNI del usuario")
    email: str = Field(..., max_length=120)
    full_name: str = Field(..., max_length=120)
    phone: str = Field(..., max_length=30)
    type: UserType = Field(...)
    timezone: str = Field(..., max_length=50)
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    email: Optional[str] = Field(None, max_length=120, description="Correo del usuario")
    full_name: Optional[str] = Field(None, max_length=120, description="Nombre completo")
    phone: Optional[str] = Field(None, max_length=30, description="Teléfono")
    type: Optional[UserType] = Field(None, description="Tipo de usuario (paciente, medico, admin)")
    timezone: Optional[str] = Field(None, max_length=50, description="Zona horaria")
    password: Optional[str] = Field(None,description="contraseña")
    model_config = ConfigDict(from_attributes=True)  

class LoginSchema(BaseModel):
    id: int
    password: str