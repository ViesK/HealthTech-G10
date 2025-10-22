from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.db import get_db
from app.modules.appointments.model import Appointment
from app.modules.appointments.schema import AppointmentCreate, AppointmentRead, AppointmentUpdate
from app.modules.appointments import service
from app.core.security import get_current_user, require_role

router = APIRouter(prefix="/appointments", tags=["appointments"], dependencies=[Depends(require_role("medico", "paciente"))])

@router.post("",response_model=AppointmentRead, status_code=status.HTTP_201_CREATED)
def create_appointment(payload: AppointmentCreate, db: Session=Depends(get_db)):
    try:
        appt = service.create_appointment(db, payload)
        return appt
    except service.InvalidTimeWindow as e:
        raise HTTPException(status_code=400, detail=str(e))
    except service.SlotAlreadyBooked as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.get("/{appointment_id}", response_model=AppointmentRead, status_code=status.HTTP_200_OK)
def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    try:
        return service.read_appointment(db, appointment_id)
    except service.NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.patch("/{appointment_id}", response_model=AppointmentRead, status_code=status.HTTP_200_OK)
def update_appointment(appointment_id: int, payload: AppointmentUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_appointment(db, appointment_id, payload)
    except service.NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except service.InvalidTimeWindow as e:
        raise HTTPException(status_code=400, detail=str(e))
    except service.SlotAlreadyBooked as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.delete("/{appointment_id}", response_model=AppointmentRead, status_code=status.HTTP_200_OK)
def cancel_appointment(appointment_id: int, db: Session = Depends(get_db)):
    try:
        return service.cancel_appointment(db, appointment_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
    except service.CannotCancelPast as e:
        raise HTTPException(400, detail=str(e))