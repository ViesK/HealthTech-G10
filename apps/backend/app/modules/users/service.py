from sqlalchemy.orm import Session
from .model import UsersModel
from .schema   import *
from typing import List, Optional
from fastapi import HTTPException, status
from app.core.security import *
from sqlalchemy.exc import IntegrityError
#Services.py maneja la lógica de acceso a datos.

#averiguar token (seguridaaad) JWT si es medico, pacientee



# GET: Traer todos los usuarios
def get_all_users(db:Session) -> List[UsersModel]:
    return db.query(UsersModel).all()

# GET: Traer un usuarios por ID
def get_user_by_id(db:Session,user_id:int) -> Optional[UsersModel]:
    return db.query(UsersModel).filter(UsersModel.id==user_id).first()

# POST: Crear un usuario
def create_user(db: Session, user_data: UserCreate) -> UsersModel:
    existing = db.query(UsersModel).filter(UsersModel.id==user_data.id).first() #Verificamos si existe el usuario 
    if existing:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    new_user = UsersModel(
        id=user_data.id,
        email=user_data.email,
        full_name=user_data.full_name,
        phone=user_data.phone,
        timezone=user_data.timezone,
        password_hash=hash_password(user_data.password),  # se convierte a hash aquí
        type=user_data.type
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except IntegrityError as e:
        db.rollback()
        # Detectamos si es duplicado de email
        if "users_email_key" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al crear el usuario"
            )


# PUT: Actualizar un usuario
def update_user(db: Session, user_id: int, user_data: UserUpdate) -> Optional[UsersModel]:
    user = db.query(UsersModel).filter(UsersModel.id == user_id).first()
    if not user:
        return None
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user
    


# DELETE: Eliminar a un usuario
def delete_user_by_id(user_id:int, db:Session) -> UsersModel:
    user = db.query(UsersModel).filter(UsersModel.id==user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True 
    return False

#Autenticar usuario
def authenticate_user(user_id: int, password: str, db: Session) -> dict:
    user = db.query(UsersModel).filter(UsersModel.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )
    if not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )

    token = create_access_token(sub=str(user.id))
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_type": user.type.value
    }