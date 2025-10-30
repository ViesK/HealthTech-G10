from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import require_role
from .schema import LocationCreate, LocationRead, LocationUpdate
from . import service

router = APIRouter(
    prefix="/locations",
    tags=["locations"],
    dependencies=[Depends(require_role("admin", "staff"))],  # ajusta si quieres
)

@router.post("", response_model=LocationRead, status_code=status.HTTP_201_CREATED)
def create_location(payload: LocationCreate, db: Session = Depends(get_db)):
    try:
        return service.create_location(db, payload)
    except service.AlreadyExists as e:
        raise HTTPException(409, detail=str(e))

@router.get("/{location_id}", response_model=LocationRead)
def read_location(location_id: int, db: Session = Depends(get_db)):
    try:
        return service.read_location(db, location_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))

@router.get("", response_model=list[LocationRead])
def list_locations(
    clinic_id: int | None = Query(None, gt=0),
    q: str | None = Query(None, description="Filtro por nombre o room_code"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return service.list_locations(db, clinic_id=clinic_id, q=q, limit=limit, offset=offset)

@router.patch("/{location_id}", response_model=LocationRead)
def update_location(location_id: int, payload: LocationUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_location(db, location_id, payload)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
    except service.AlreadyExists as e:
        raise HTTPException(409, detail=str(e))

@router.delete("/{location_id}", response_model=LocationRead)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    try:
        return service.delete_location(db, location_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
