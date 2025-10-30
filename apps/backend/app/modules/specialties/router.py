from fastapi import APIRouter
router = APIRouter(prefix="/specialties", tags=["specialties"])
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import require_role
from .schema import SpecialtyCreate, SpecialtyRead, SpecialtyUpdate
from . import service

router = APIRouter(
    prefix="/specialties",
    tags=["specialties"],
    dependencies=[Depends(require_role("admin", "staff"))],  # ajusta roles si quieres
)

@router.post("", response_model=SpecialtyRead, status_code=status.HTTP_201_CREATED)
def create_specialty(payload: SpecialtyCreate, db: Session = Depends(get_db)):
    try:
        return service.create_specialty(db, payload)
    except service.AlreadyExists as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/{specialty_id}", response_model=SpecialtyRead)
def read_specialty(specialty_id: int, db: Session = Depends(get_db)):
    try:
        return service.read_specialty(db, specialty_id)
    except service.NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("", response_model=list[SpecialtyRead])
def list_specialties(
    q: str | None = Query(None, description="Filtro por nombre (ilike)"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return service.list_specialties(db, q=q, limit=limit, offset=offset)


@router.patch("/{specialty_id}", response_model=SpecialtyRead)
def update_specialty(specialty_id: int, payload: SpecialtyUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_specialty(db, specialty_id, payload)
    except service.NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except service.AlreadyExists as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.delete("/{specialty_id}", response_model=SpecialtyRead)
def delete_specialty(specialty_id: int, db: Session = Depends(get_db)):
    try:
        return service.delete_specialty(db, specialty_id)
    except service.NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
