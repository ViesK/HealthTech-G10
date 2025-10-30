from sqlalchemy.orm import Session
from .model import *
from .schema   import *
from typing import List, Optional

#Services.py maneja la lógica de acceso a datos.

# GET: Traer todas las clinicas 
def get_all_clinics(db:Session) -> List[ClinicModel]:
    return db.query(ClinicModel).all()

# GET: Traer una clinica por ID
def get_clinic_by_id(db:Session,clinic_id:int) -> ClinicModel:
    return db.query(ClinicModel).filter(ClinicModel.id==clinic_id).first()

# POST: Crear una clinica
def create_clinic(db:Session,user_data:ClinicCreate) -> ClinicModel:
    clinic = ClinicModel(**user_data.dict())
    db.add(clinic)
    db.commit()
    db.refresh(clinic)
    return clinic

# PUT: Actualizar una clinica
def update_clinic(db:Session,clinic_id:int,clinic_data:ClinicUpdate) -> Optional[ClinicModel]:
    clinic = db.query(ClinicModel).filter(ClinicModel.id==clinic_id).first()
    if not clinic:
        return None
    for key, value in clinic_data.dict(exclude_unset=True).items():
        setattr(clinic, key, value)
    db.commit()
    db.refresh(clinic)
    return clinic

# DELETE: Eliminar una clinica
def delete_clinic(db:Session,clinic_id:int) ->ClinicModel:
    clinic = db.query(ClinicModel).filter(ClinicModel.id==clinic_id).first()
    if clinic:
        db.delete(clinic)
        db.commit()
        return True
    return False