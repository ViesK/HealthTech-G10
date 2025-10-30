from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List

from app.core.db import get_db
from app.core.security import require_role
from .schema import MedicSpecialtyCreate, MedicSpecialtyRead, MedicSpecialtyUpdate
from . import service

router = APIRouter(
    prefix="/medic-specialties",
    tags=["medic_specialties"],
    dependencies=[Depends(require_role("admin", "staff"))],  # ajusta si quieres
)

@router.post("", response_model=MedicSpecialtyRead, status_code=status.HTTP_201_CREATED)
def create_medic_specialty(payload: MedicSpecialtyCreate, db: Session = Depends(get_db)):
    try:
        return service.create_ms(db, payload)
    except service.InvalidMedicRole as e:
        raise HTTPException(400, detail=str(e))
    except service.ClinicDoesNotOfferSpecialty as e:
        raise HTTPException(400, detail=str(e))
    except service.AlreadyExists as e:
        raise HTTPException(409, detail=str(e))

@router.get("/{ms_id}", response_model=MedicSpecialtyRead)
def read_medic_specialty(ms_id: int, db: Session = Depends(get_db)):
    try:
        return service.read_ms(db, ms_id)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))

@router.get("", response_model=List[MedicSpecialtyRead])
def list_medic_specialties(
    clinic_id: int | None = Query(None, gt=0),
    medical_user_id: int | None = Query(None, gt=0),
    specialty_id: int | None = Query(None, gt=0),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return service.list_ms(
        db,
        clinic_id=clinic_id,
        medical_user_id=medical_user_id,
        specialty_id=specialty_id,
        limit=limit,
        offset=offset,
    )

@router.patch("/{ms_id}", response_model=MedicSpecialtyRead)
def update_medic_specialty(ms_id: int, payload: MedicSpecialtyUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_ms(db, ms_id, payload)
    except service.NotFound as e:
        raise HTTPException(404, detail=str(e))
    except service.InvalidMedicRole as e:
        raise HTTPException(400, detail=str(e))
    except service.ClinicDoesNotOfferSpecialty as e:
        raise HTTPException(400, detail=str(e))
    except service.AlreadyExists as e:
        raise HTTPException(409, detail=str(e))

@router.delete("/{ms_id}")
def delete_medic_specialty(ms_id: int, db: Session = Depends(get_db)):
    ok = service.delete_ms(db, ms_id)
    if not ok:
        raise HTTPException(404, detail="MedicSpecialty no encontrado")
    return {"message": f"MedicSpecialty {ms_id} eliminado correctamente"}
