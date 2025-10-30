# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_PREFIX = "/api"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://salud:salud@localhost:5432/salud")
JWT_SECRET = os.getenv("JWT_SECRET", "CHANGE_ME")
CORS_ORIGINS = ["http://localhost:5173"]

