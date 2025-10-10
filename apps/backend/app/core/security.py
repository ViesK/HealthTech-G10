# app/core/security.py
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt
from .config import JWT_SECRET

_ALG = "HS256"
_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    return _pwd.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return _pwd.verify(plain, hashed)

def create_access_token(sub: str, minutes: int = 60) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": sub, "iat": int(now.timestamp()), "exp": int((now + timedelta(minutes=minutes)).timestamp())}
    return jwt.encode(payload, JWT_SECRET, algorithm=_ALG)

def decode_token(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET, algorithms=[_ALG])
