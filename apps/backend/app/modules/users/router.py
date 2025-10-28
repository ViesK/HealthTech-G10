from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
# Modelos SQLAlchemy
from .model import UsersModel  # <-- tu modelo de la tabla users
# Schemas Pydantic
from .schema import *  # <-- schema para validar/serializar datos
# Services
from  .service import *
# Función para obtener sesión DB
from app.core.security import *
from app.core.db import get_db

router = APIRouter(prefix="/users", tags=["users"])
#router = APIRouter(prefix="/users", tags=["users"], dependencies=[Depends(get_current_user)])

#RUTAS PROTEGIDAS -> Linea 65

# Route GET ALL
@router.get("/", response_model=List[UserSchema]) #Al devolver varios se pone [UserSchema]
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

# GET: Traer un usuario por ID
@router.get("/{user_id}",  response_model=UserSchema)  #Al devolver uno se pone UserSchema
def get_user(user_id:int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id) 
    if not user:
        return HTTPException(status_code=404, detail="No existe el usuario")
    return user

# POST: crear un usuario
@router.post("/", response_model=UserSchema)
def create_user_by_id(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)
     
# PUT: actualizar usuario
@router.put("/{user_id}", response_model=UserSchema)
def update_user_route(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    updated = update_user(db, user_id, user_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated

# DELETE: Eliminar a un usuario
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = delete_user_by_id(user_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="No existe el usuario")
    return {"message": f"Usuario con id {user_id} eliminado correctamente"}

#LOGIN: logearse
@router.post("/login")
def login(data: LoginSchema, db:Session=Depends(get_db)):
    return  authenticate_user(data.id,data.password,db)
    
#REGISTER
#Si tira error porque supera 72 -> py -m pipenv install bcrypt==4.0.1 passlib==1.7.4
@router.post("/register", response_model=UserSchema)
def register(data: UserCreate,db:Session=Depends(get_db)):
    return create_user(db,data)

#RUTAS PROTEGIDAS
medico_router = APIRouter(prefix="/medicos", tags=["medico"])
paciente_router = APIRouter(prefix="/pacientes", tags=["paciente"])


#para medico
@medico_router.get("/dashboard", response_model=dict)
def medico_dashboard(user=Depends(require_role("medico"))):
    return {"msg": f"Bienvenido doctor {user['sub']}"}

#Para paciente
@paciente_router.get("/dashboard", response_model=dict)
def paciente_dashboard(user=Depends(require_role("paciente"))):
    return {"msg": f"Bienvenido paciente {user['sub']}"}
