from sqlalchemy import select
from sqlalchemy.orm import Session
from .model import Location as LocationModel
from .schema import LocationCreate, LocationUpdate

class NotFound(Exception): ...
class AlreadyExists(Exception): ...

def _get_or_404(db: Session, location_id: int) -> LocationModel:
    loc = db.get(LocationModel, location_id)
    if not loc:
        raise NotFound("Location no encontrada")
    return loc

def _exists_name_in_clinic(db: Session, clinic_id: int, name: str, exclude_id: int | None = None) -> bool:
    stmt = select(LocationModel.id).where(
        LocationModel.clinic_id == clinic_id,
        LocationModel.name == name,
    ).limit(1)
    if exclude_id is not None:
        stmt = stmt.where(LocationModel.id != exclude_id)
    return db.scalar(stmt) is not None

def create_location(db: Session, payload: LocationCreate) -> LocationModel:
    if _exists_name_in_clinic(db, payload.clinic_id, payload.name):
        raise AlreadyExists("Ya existe una ubicación con ese nombre en la clínica")
    loc = LocationModel(**payload.model_dump())
    db.add(loc)
    db.commit()
    db.refresh(loc)
    return loc

def read_location(db: Session, location_id: int) -> LocationModel:
    return _get_or_404(db, location_id)

def list_locations(
    db: Session,
    clinic_id: int | None = None,
    q: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> list[LocationModel]:
    stmt = select(LocationModel)
    if clinic_id is not None:
        stmt = stmt.where(LocationModel.clinic_id == clinic_id)
    if q:
        # búsqueda simple por nombre / room_code
        like = f"%{q}%"
        stmt = stmt.where((LocationModel.name.ilike(like)) | (LocationModel.room_code.ilike(like)))
    stmt = stmt.order_by(LocationModel.name).limit(limit).offset(offset)
    return list(db.scalars(stmt).all())

def update_location(db: Session, location_id: int, payload: LocationUpdate) -> LocationModel:
    loc = _get_or_404(db, location_id)
    data = payload.model_dump(exclude_unset=True)

    new_clinic = data.get("clinic_id", loc.clinic_id)
    new_name = data.get("name", loc.name)

    if _exists_name_in_clinic(db, new_clinic, new_name, exclude_id=loc.id):
        raise AlreadyExists("Ya existe una ubicación con ese nombre en la clínica")

    for k, v in data.items():
        setattr(loc, k, v)

    db.commit()
    db.refresh(loc)
    return loc

def delete_location(db: Session, location_id: int) -> LocationModel:
    loc = _get_or_404(db, location_id)
    db.delete(loc)
    db.commit()
    return loc

