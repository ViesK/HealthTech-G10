from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .service import *
from .schema import *
from app.core.db import get_db

router = APIRouter(prefix="/clinic", tags=["clinic"])
 

# GET: Traer todas las clinicas 
@router.get("/", response_model=List[ClinicSchema])
def get_clinics(db: Session=Depends(get_db)):
    return get_all_clinics(db)
   

# GET: Traer una clinica por ID
@router.get("/{clinic_id}",response_model=ClinicSchema)
def get_clinic(clinic_id:int, db: Session=Depends(get_db)):
    clinic = get_clinic_by_id(db,clinic_id)
    if not clinic:
         return HTTPException(status_code=404, detail="No existe la clinica")
    return clinic

# POST: Crear una clinica
@router.post("/", response_model=ClinicCreate)
def create_user(clinic_data:ClinicCreate, db:Session=Depends(get_db)):
    clinic = create_clinic(db,clinic_data)
    return clinic

# PUT: Actualizar un usuario
@router.put("/{clinic_id}", response_model=ClinicSchema)
def update_clinic(clinic_id: int, updated_user: ClinicUpdate, db: Session = Depends(get_db)):
    update = update_clinic(db,clinic_id,updated_user)
    if not update:
        raise HTTPException(status_code=404, detail="Clinica no encontrada")
    return update
# DELETE: Eliminar a un usuario

@router.delete("/{clinic_id}")
def delete_clinic(clinic_id: int, db: Session = Depends(get_db)):
    clinic = db.query(ClinicModel).filter(ClinicModel.id == clinic_id).first()
    if not clinic:
          raise HTTPException(status_code=404, detail="No existe la clinica")
    return {"message": f"Clinica con id {clinic_id} eliminado correctamente"}
