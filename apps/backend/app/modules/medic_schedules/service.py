from sqlalchemy.orm import Session
from typing import List, Optional
from .model import Medic_SchedulesModel
from .schema import MedicScheduleCreate, MedicScheduleUpdate

# POST: Crear horario
def create_schedule(db: Session, schedule_data: MedicScheduleCreate) -> Medic_SchedulesModel:
    schedule = Medic_SchedulesModel(**schedule_data.dict())
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule

# GET: todos los horarios
def get_all_schedules(db: Session) -> List[Medic_SchedulesModel]:
    return db.query(Medic_SchedulesModel).all()

# GET: Obtener horario por ID DE TABLA
def get_schedule_by_id(db: Session, schedule_id: int) -> Optional[Medic_SchedulesModel]:
    return db.query(Medic_SchedulesModel).filter(Medic_SchedulesModel.id == schedule_id).first()

# GET: Obtener horario por ID POR MEDICO
def get_medic_schedule_by_id(db:Session,medic_id:int)-> Optional[Medic_SchedulesModel]:
    return db.query(Medic_SchedulesModel).filter(Medic_SchedulesModel.medic_user_id==medic_id).all()

# Actualizar horario
def update_schedule(db: Session, schedule_id: int, update_data: MedicScheduleUpdate) -> Optional[Medic_SchedulesModel]:
    schedule = db.query(Medic_SchedulesModel).filter(Medic_SchedulesModel.id == schedule_id).first()
    if not schedule:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(schedule, key, value)
    db.commit()
    db.refresh(schedule)
    return schedule

# Borrar horario
def delete_schedule(db: Session, schedule_id: int) -> bool:
    schedule = db.query(Medic_SchedulesModel).filter(Medic_SchedulesModel.id == schedule_id).first()
    if not schedule:
        return False
    db.delete(schedule)
    db.commit()
    return True