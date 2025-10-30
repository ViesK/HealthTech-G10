from sqlalchemy import select
from sqlalchemy.orm import Session
from .model import Specialty as SpecialtyModel
from .schema import SpecialtyCreate, SpecialtyUpdate


class NotFound(Exception): ...
class AlreadyExists(Exception): ...


# ______________ Helpers ______________
def _get_or_404(db: Session, specialty_id: int) -> SpecialtyModel:
    sp = db.get(SpecialtyModel, specialty_id)
    if not sp:
        raise NotFound("Specialty no encontrada")
    return sp


# ______________ CRUD ______________
def create_specialty(db: Session, payload: SpecialtyCreate) -> SpecialtyModel:
    exists = db.scalar(select(SpecialtyModel.id).where(SpecialtyModel.name == payload.name))
    if exists is not None:
        raise AlreadyExists("Ya existe una especialidad con ese nombre")

    sp = SpecialtyModel(**payload.model_dump())
    db.add(sp)
    db.commit()
    db.refresh(sp)
    return sp


def read_specialty(db: Session, specialty_id: int) -> SpecialtyModel:
    return _get_or_404(db, specialty_id)


def list_specialties(db: Session, q: str | None = None, limit: int = 50, offset: int = 0) -> list[SpecialtyModel]:
    stmt = select(SpecialtyModel).order_by(SpecialtyModel.name).limit(limit).offset(offset)
    if q:
        # Búsqueda simple por prefijo/substring (case-insensitive depende del collation de la DB)
        stmt = select(SpecialtyModel).where(SpecialtyModel.name.ilike(f"%{q}%")).order_by(SpecialtyModel.name).limit(limit).offset(offset)
    return list(db.scalars(stmt).all())


def update_specialty(db: Session, specialty_id: int, payload: SpecialtyUpdate) -> SpecialtyModel:
    sp = _get_or_404(db, specialty_id)
    data = payload.model_dump(exclude_unset=True)

    if "name" in data and data["name"] != sp.name:
        dup = db.scalar(select(SpecialtyModel.id).where(SpecialtyModel.name == data["name"]))
        if dup is not None:
            raise AlreadyExists("Ya existe una especialidad con ese nombre")

    for k, v in data.items():
        setattr(sp, k, v)

    db.commit()
    db.refresh(sp)
    return sp


def delete_specialty(db: Session, specialty_id: int) -> SpecialtyModel:
    sp = _get_or_404(db, specialty_id)
    db.delete(sp)
    db.commit()
    return sp
