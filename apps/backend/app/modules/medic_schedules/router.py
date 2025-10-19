from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .service import *
from .schema import *
from app.core.db import get_db
from app.core.security import require_role, get_current_user, create_access_token

router = APIRouter(prefix="/medic_schedules", tags=["medic_schedules"])

#GET Traer todo los horarios
@router.get("/",response_model=List[MedicScheduleSchema])
def get_schedules(db: Session=Depends(get_db)):
    return get_all_schedules(db)

#GET Traer por ID (NO ES POR MEDICO)
@router.get("/",response_model=MedicScheduleSchema)
def get_schedules(schedule_id:int,db: Session=Depends(get_db),):
    return get_schedule_by_id(db,schedule_id)

#GET Traer horarios del medico
@router.get("/",response_model=List[MedicScheduleSchema])
def get_schedules(medic_id:int,db: Session=Depends(get_db)):
    return get_medic_schedule_by_id(db,medic_id)

#GET RUTA PROTEGIDA POR JTW <-------------------------------------
@router.get("/schedules", dependencies=[Depends(require_role("medico"))])
def get_schedules_for_medic():
    return {"msg": "Solo los médicos pueden ver esto"}

#POST Crear horario
@router.post("/",response_model=MedicScheduleCreate)
def create_medic_schedule(schedule_medic:MedicScheduleCreate, db: Session=Depends(get_db)):
    schedule = create_schedule(db,schedule_medic)
    return schedule

#PUT Actualizar horario
@router.put("/{schedule_id}",response_model=MedicScheduleSchema)
def update_medic_schedule(schedule_id:int,schedule_update:MedicScheduleUpdate,db: Session=Depends(get_db)):
    update = update_schedule(db,schedule_id,update_schedule) 
    if not update:
        raise HTTPException(status_code=404, detail="horario no encontrada")
    return update

@router.delete("/{schedule_id}")
def delete_medic_schedule(schedule_id:int,db: Session=Depends(get_db)):
    schedule = delete_schedule(db,schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="No existe el horario")
    return {"message": f"Horario con id {schedule_id} eliminado correctamente"}
