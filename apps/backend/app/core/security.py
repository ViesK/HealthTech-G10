# app/core/security.py
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt
from .config import JWT_SECRET
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Callable
_ALG = "HS256"

# Endpoint de login para obtener el token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return _pwd.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return _pwd.verify(plain, hashed)

def create_access_token(sub: str, minutes: int = 60, **claims) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": sub, "iat": int(now.timestamp()), "exp": int((now + timedelta(minutes=minutes)).timestamp()),**claims}
    return jwt.encode(payload, JWT_SECRET, algorithm=_ALG)

def decode_token(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET, algorithms=[_ALG])

# --- DEPENDENCIAS PARA RUTAS ---
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """Devuelve la información del usuario autenticado desde el token."""
    payload = decode_token(token)
    return payload

def require_role(*allowed_roles: str) -> Callable:

    allowed = {str(r) for r in allowed_roles}

    def role_checker(payload: dict = Depends(get_current_user)):
        user_type = payload.get("type")
        if user_type not in allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permisos insuficientes. Requiere uno de: {', '.join(sorted(allowed))}"
            )
        return payload
    return role_checker