from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.db import get_db
from app.core.security import require_role
from .schema import ServiceSlotCreate, ServiceSlotRead, ServiceSlotUpdate
from . import service

router = APIRouter(
    prefix="/service-slots",
    tags=["service_slots"],
    dependencies=[Depends(require_role("admin", "staff"))],  # ajusta si quieres
)

@router.post("", response_model=ServiceSlotRead, status_code=status.HTTP_201_CREATED)
def create_slot(payload: ServiceSlotCreate, db: Session = Depends(get_db)):
    try:
        return service.create_slot(db, payload)
    except service.InvalidTimeWindow as e:
        raise HTTPException(400, detail=str(e))
    except service.OverlappingSlot as e:
        raise HTTPException(409, detail=str(e))

@router.get("/{slot_id}", response_model=ServiceSlotRead)
def read_slot(slot_id: int, db: Session = Depends(get_db)):
    try:
        return service.read_slot(db, slot_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))

@router.get("", response_model=list[ServiceSlotRead])
def list_slots(
    clinic_id: int | None = Query(None, gt=0),
    specialty_id: int | None = Query(None, gt=0),
    date_from: datetime | None = Query(None),
    date_to: datetime | None = Query(None),
    status: str | None = Query(None),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return service.list_slots(
        db,
        clinic_id=clinic_id,
        specialty_id=specialty_id,
        date_from=date_from,
        date_to=date_to,
        status=status,
        limit=limit,
        offset=offset,
    )

@router.patch("/{slot_id}", response_model=ServiceSlotRead)
def update_slot(slot_id: int, payload: ServiceSlotUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_slot(db, slot_id, payload)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
    except service.InvalidTimeWindow as e:
        raise HTTPException(400, detail=str(e))
    except service.OverlappingSlot as e:
        raise HTTPException(409, detail=str(e))

@router.delete("/{slot_id}", response_model=ServiceSlotRead)
def delete_slot(slot_id: int, db: Session = Depends(get_db)):
    try:
        return service.delete_slot(db, slot_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))

# ---- cambios rápidos de estado ----
@router.post("/{slot_id}/open", response_model=ServiceSlotRead)
def open_slot(slot_id: int, db: Session = Depends(get_db)):
    try:
        return service.set_status(db, slot_id, "OPEN", held_until=None)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))

@router.post("/{slot_id}/hold", response_model=ServiceSlotRead)
def hold_slot(slot_id: int, held_until: datetime | None = None, db: Session = Depends(get_db)):
    try:
        return service.set_status(db, slot_id, "HELD", held_until=held_until)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))

@router.post("/{slot_id}/block", response_model=ServiceSlotRead)
def block_slot(slot_id: int, db: Session = Depends(get_db)):
    try:
        return service.set_status(db, slot_id, "BLOCKED", held_until=None)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
