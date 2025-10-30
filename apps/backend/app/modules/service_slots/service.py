from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime
from .model import ServiceSlot as SlotModel
from .schema import ServiceSlotCreate, ServiceSlotUpdate

class NotFound(Exception): ...
class InvalidTimeWindow(Exception): ...
class OverlappingSlot(Exception): ...
class InvalidStatus(Exception): ...

# -------- helpers --------
def _get_or_404(db: Session, slot_id: int) -> SlotModel:
    slot = db.get(SlotModel, slot_id)
    if not slot:
        raise NotFound("ServiceSlot no encontrado")
    return slot

def _validate_time_window(start_ts: datetime, end_ts: datetime):
    if end_ts <= start_ts:
        raise InvalidTimeWindow("La fecha de inicio debe ser anterior a la fecha de fin")

def _overlap_exists(db: Session, clinic_id: int, specialty_id: int, start_ts: datetime, end_ts: datetime, exclude_id: int | None = None) -> bool:
    stmt = (
        select(SlotModel.id)
        .where(
            SlotModel.clinic_id == clinic_id,
            SlotModel.specialty_id == specialty_id,
            SlotModel.start_ts < end_ts,
            SlotModel.end_ts   > start_ts,
        )
        .limit(1)
    )
    if exclude_id is not None:
        stmt = stmt.where(SlotModel.id != exclude_id)
    return db.scalar(stmt) is not None

# -------- CRUD --------
def create_slot(db: Session, payload: ServiceSlotCreate) -> SlotModel:
    _validate_time_window(payload.start_ts, payload.end_ts)

    if _overlap_exists(db, payload.clinic_id, payload.specialty_id, payload.start_ts, payload.end_ts):
        raise OverlappingSlot("Ya existe otro ServiceSlot que se solapa en ese rango")

    slot = SlotModel(**payload.model_dump())
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot

def read_slot(db: Session, slot_id: int) -> SlotModel:
    return _get_or_404(db, slot_id)

def list_slots(
    db: Session,
    clinic_id: int | None = None,
    specialty_id: int | None = None,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
    status: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[SlotModel]:
    stmt = select(SlotModel)

    if clinic_id is not None:
        stmt = stmt.where(SlotModel.clinic_id == clinic_id)
    if specialty_id is not None:
        stmt = stmt.where(SlotModel.specialty_id == specialty_id)
    if status is not None:
        stmt = stmt.where(SlotModel.status == status)

    # rango de fechas opcional
    if date_from is not None:
        stmt = stmt.where(SlotModel.end_ts > date_from)
    if date_to is not None:
        stmt = stmt.where(SlotModel.start_ts < date_to)

    stmt = stmt.order_by(SlotModel.start_ts).limit(limit).offset(offset)
    return list(db.scalars(stmt).all())

def update_slot(db: Session, slot_id: int, payload: ServiceSlotUpdate) -> SlotModel:
    slot = _get_or_404(db, slot_id)
    data = payload.model_dump(exclude_unset=True)

    new_start = data.get("start_ts", slot.start_ts)
    new_end   = data.get("end_ts", slot.end_ts)
    new_clinic = data.get("clinic_id", slot.clinic_id)
    new_spec   = data.get("specialty_id", slot.specialty_id)

    _validate_time_window(new_start, new_end)

    if _overlap_exists(db, new_clinic, new_spec, new_start, new_end, exclude_id=slot.id):
        raise OverlappingSlot("Se solapa con otro ServiceSlot existente")

    for k, v in data.items():
        setattr(slot, k, v)

    db.commit()
    db.refresh(slot)
    return slot

def delete_slot(db: Session, slot_id: int) -> SlotModel:
    slot = _get_or_404(db, slot_id)
    db.delete(slot)
    db.commit()
    return slot

# -------- estado rápido --------
def set_status(db: Session, slot_id: int, new_status: str, held_until: datetime | None = None) -> SlotModel:
    if new_status not in ("OPEN", "HELD", "BLOCKED"):
        raise InvalidStatus("Estado no válido")
    slot = _get_or_404(db, slot_id)
    slot.status = new_status
    slot.held_until = held_until
    db.commit()
    db.refresh(slot)
    return slot
