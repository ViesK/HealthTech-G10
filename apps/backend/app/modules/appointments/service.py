from sqlalchemy import select
from sqlalchemy.orm import Session
from .model import Appointment as AppointmentModel
from .schema import AppointmentCreate, AppointmentUpdate

class InvalidTimeWindow(Exception): ...
class SlotAlreadyBooked(Exception): ...
class NotFound(Exception): ...
class CannotCancelPast(Exception): ...

#_____________________Funciones Globales_____________________
def _validate_time_window(start_ts, end_ts) -> None:
    if end_ts <= start_ts:
        raise InvalidTimeWindow("La fecha de inicio debe ser anterior a la fecha de finalización")

def _get_or_404(db: Session, appt_id: int) -> AppointmentModel:
    appt = db.get(AppointmentModel, appt_id)
    if not appt:
        raise NotFound("Appointment no encontrado")
    return appt

#_____________________Funciones CRUD_____________________
def create_appointment(db, payload: AppointmentCreate) -> AppointmentModel:

    _validate_time_window(payload.start_ts, payload.end_ts)
    
    exists = db.execute(
        select(AppointmentModel.id).where(
            AppointmentModel.service_slot_id == payload.service_slot_id,
            AppointmentModel.start_ts == payload.start_ts,
            AppointmentModel.end_ts == payload.end_ts,
        )
    ).first()
    if exists:
        raise SlotAlreadyBooked("Ya existe una cita en esa fecha y hora.")

    appt = AppointmentModel(**payload.model_dump())
    db.add(appt)
    db.commit()
    db.refresh(appt)
    return appt

def read_appointment(db: Session, appt_id: int) -> AppointmentModel:
    return _get_or_404(db, appt_id)

def update_appointment(db: Session, appt_id: int, payload: AppointmentUpdate) -> AppointmentModel:
    appt = _get_or_404(db, appt_id)
    
    data = payload.model_dump(exclude_unset=True)

    new_start = data.get("start_ts", appt.start_ts)
    new_end   = data.get("end_ts", appt.end_ts)
    new_slot  = data.get("service_slot_id", appt.service_slot_id)

    _validate_time_window(new_start, new_end)
    
    overlap = db.scalar(
        select(AppointmentModel.id)
        .where(
            AppointmentModel.service_slot_id == new_slot,
            AppointmentModel.start_ts < new_end,
            AppointmentModel.end_ts   > new_start,
            AppointmentModel.id != appt.id,
        )
        .limit(1)
    )
    if overlap is not None:
        raise SlotAlreadyBooked("Ya existe una cita en esa fecha y hora")
    
    for k, v in data.items():
        setattr(appt, k, v)

    db.commit()
    db.refresh(appt)
    return appt

def cancel_appointment(db: Session, appt_id: int) -> AppointmentModel:
    appt = _get_or_404(db, appt_id)
    
    from datetime import datetime, timezone
    if appt.start_ts <= datetime.now(appt.start_ts.tzinfo or timezone.utc):
        raise CannotCancelPast("No se puede cancelar una cita pasada o en curso")

    if appt.status != "CANCELLED":
        appt.status = "CANCELLED"
        db.commit()
        db.refresh(appt)
    return appt

