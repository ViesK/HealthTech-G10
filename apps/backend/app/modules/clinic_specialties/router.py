from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import require_role
from .schema import ClinicSpecialtyCreate, ClinicSpecialtyRead, ClinicSpecialtyUpdate
from . import service

router = APIRouter(
    prefix="/clinic-specialties",
    tags=["clinic_specialties"],
    dependencies=[Depends(require_role("admin", "staff"))],
)

@router.post("", response_model=ClinicSpecialtyRead, status_code=status.HTTP_201_CREATED)
def create_cs(payload: ClinicSpecialtyCreate, db: Session = Depends(get_db)):
    try:
        return service.create_cs(db, payload)
    except service.AlreadyExists as e:
        raise HTTPException(409, detail=str(e))

@router.get("/{cs_id}", response_model=ClinicSpecialtyRead)
def read_cs(cs_id: int, db: Session = Depends(get_db)):
    try:
        return service.read_cs(db, cs_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))

@router.get("", response_model=list[ClinicSpecialtyRead])
def list_cs(
    clinic_id: int | None = Query(None, gt=0),
    specialty_id: int | None = Query(None, gt=0),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return service.list_cs(db, clinic_id=clinic_id, specialty_id=specialty_id, limit=limit, offset=offset)

@router.patch("/{cs_id}", response_model=ClinicSpecialtyRead)
def update_cs(cs_id: int, payload: ClinicSpecialtyUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_cs(db, cs_id, payload)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
    except service.AlreadyExists as e:
        raise HTTPException(409, detail=str(e))

@router.delete("/{cs_id}", response_model=ClinicSpecialtyRead)
def delete_cs(cs_id: int, db: Session = Depends(get_db)):
    try:
        return service.delete_cs(db, cs_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
