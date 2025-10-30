from sqlalchemy import select
from sqlalchemy.orm import Session
from .model import ClinicSpecialty as CSModel
from .schema import ClinicSpecialtyCreate, ClinicSpecialtyUpdate

class NotFound(Exception): ...
class AlreadyExists(Exception): ...

def _get_or_404(db: Session, cs_id: int) -> CSModel:
    row = db.get(CSModel, cs_id)
    if not row:
        raise NotFound("ClinicSpecialty no encontrado")
    return row

def _exists_pair(db: Session, clinic_id: int, specialty_id: int, exclude_id: int | None = None) -> bool:
    stmt = (
        select(CSModel.id)
        .where(
            CSModel.clinic_id == clinic_id,
            CSModel.specialty_id == specialty_id,
        )
        .limit(1)
    )
    if exclude_id is not None:
        stmt = stmt.where(CSModel.id != exclude_id)
    return db.scalar(stmt) is not None

def create_cs(db: Session, payload: ClinicSpecialtyCreate) -> CSModel:
    if _exists_pair(db, payload.clinic_id, payload.specialty_id):
        raise AlreadyExists("La clínica ya ofrece esa especialidad")
    row = CSModel(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def read_cs(db: Session, cs_id: int) -> CSModel:
    return _get_or_404(db, cs_id)

def list_cs(
    db: Session,
    clinic_id: int | None = None,
    specialty_id: int | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[CSModel]:
    stmt = select(CSModel)
    if clinic_id is not None:
        stmt = stmt.where(CSModel.clinic_id == clinic_id)
    if specialty_id is not None:
        stmt = stmt.where(CSModel.specialty_id == specialty_id)
    stmt = stmt.order_by(CSModel.clinic_id, CSModel.specialty_id).limit(limit).offset(offset)
    return list(db.scalars(stmt).all())

def update_cs(db: Session, cs_id: int, payload: ClinicSpecialtyUpdate) -> CSModel:
    row = _get_or_404(db, cs_id)
    data = payload.model_dump(exclude_unset=True)

    new_clinic = data.get("clinic_id", row.clinic_id)
    new_spec   = data.get("specialty_id", row.specialty_id)

    if _exists_pair(db, new_clinic, new_spec, exclude_id=row.id):
        raise AlreadyExists("La clínica ya ofrece esa especialidad")

    for k, v in data.items():
        setattr(row, k, v)

    db.commit()
    db.refresh(row)
    return row

def delete_cs(db: Session, cs_id: int) -> CSModel:
    row = _get_or_404(db, cs_id)
    db.delete(row)
    db.commit()
    return row
