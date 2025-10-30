from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List, Optional

from .model import MedicSpecialty as MSModel
from .schema import MedicSpecialtyCreate, MedicSpecialtyUpdate

# Validaciones ligeras contra otros módulos
from app.modules.users.model import UsersModel, UserType
from app.modules.clinic_specialties.model import ClinicSpecialty as CSModel

class NotFound(Exception): ...
class AlreadyExists(Exception): ...
class InvalidMedicRole(Exception): ...
class ClinicDoesNotOfferSpecialty(Exception): ...

def _get_or_404(db: Session, ms_id: int) -> MSModel:
    row = db.get(MSModel, ms_id)
    if not row:
        raise NotFound("MedicSpecialty no encontrado")
    return row

def _exists_combo(db: Session, clinic_id: int, medical_user_id: int, specialty_id: int, exclude_id: Optional[int] = None) -> bool:
    stmt = (
        select(MSModel.id)
        .where(
            MSModel.clinic_id == clinic_id,
            MSModel.medical_user_id == medical_user_id,
            MSModel.specialty_id == specialty_id,
        )
        .limit(1)
    )
    if exclude_id is not None:
        stmt = stmt.where(MSModel.id != exclude_id)
    return db.scalar(stmt) is not None

def _assert_medic_role(db: Session, medical_user_id: int):
    user_type = db.scalar(select(UsersModel.type).where(UsersModel.id == medical_user_id))
    if user_type is None or user_type != UserType.medico:
        raise InvalidMedicRole("El usuario no tiene rol de médico")

def _assert_clinic_offers_specialty(db: Session, clinic_id: int, specialty_id: int):
    exists = db.scalar(
        select(CSModel.id).where(
            CSModel.clinic_id == clinic_id,
            CSModel.specialty_id == specialty_id,
        )
    )
    if exists is None:
        raise ClinicDoesNotOfferSpecialty("La clínica no ofrece esa especialidad")

# ------------- CRUD -------------
def create_ms(db: Session, payload: MedicSpecialtyCreate) -> MSModel:
    _assert_medic_role(db, payload.medical_user_id)
    _assert_clinic_offers_specialty(db, payload.clinic_id, payload.specialty_id)

    if _exists_combo(db, payload.clinic_id, payload.medical_user_id, payload.specialty_id):
        raise AlreadyExists("Ya existe esa asignación médico–especialidad en la clínica")

    row = MSModel(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def read_ms(db: Session, ms_id: int) -> MSModel:
    return _get_or_404(db, ms_id)

def list_ms(
    db: Session,
    clinic_id: Optional[int] = None,
    medical_user_id: Optional[int] = None,
    specialty_id: Optional[int] = None,
    limit: int = 100,
    offset: int = 0,
) -> List[MSModel]:
    stmt = select(MSModel)
    if clinic_id is not None:
        stmt = stmt.where(MSModel.clinic_id == clinic_id)
    if medical_user_id is not None:
        stmt = stmt.where(MSModel.medical_user_id == medical_user_id)
    if specialty_id is not None:
        stmt = stmt.where(MSModel.specialty_id == specialty_id)
    stmt = stmt.order_by(MSModel.medical_user_id, MSModel.clinic_id, MSModel.specialty_id).limit(limit).offset(offset)
    return list(db.scalars(stmt).all())

def update_ms(db: Session, ms_id: int, payload: MedicSpecialtyUpdate) -> MSModel:
    row = _get_or_404(db, ms_id)
    data = payload.model_dump(exclude_unset=True)

    new_clinic = data.get("clinic_id", row.clinic_id)
    new_medic  = data.get("medical_user_id", row.medical_user_id)
    new_spec   = data.get("specialty_id", row.specialty_id)

    # Validaciones solo si cambian campos clave
    if "medical_user_id" in data:
        _assert_medic_role(db, new_medic)
    if "clinic_id" in data or "specialty_id" in data:
        _assert_clinic_offers_specialty(db, new_clinic, new_spec)

    if _exists_combo(db, new_clinic, new_medic, new_spec, exclude_id=row.id):
        raise AlreadyExists("Ya existe esa asignación médico–especialidad en la clínica")

    for k, v in data.items():
        setattr(row, k, v)

    db.commit()
    db.refresh(row)
    return row

def delete_ms(db: Session, ms_id: int) -> bool:
    row = db.get(MSModel, ms_id)
    if not row:
        return False
    db.delete(row)
    db.commit()
    return True
