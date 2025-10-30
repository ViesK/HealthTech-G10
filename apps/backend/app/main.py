from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import API_PREFIX, CORS_ORIGINS

app = FastAPI(title="HealthTech API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .modules import models_registry as _models_registry

from .modules import ROUTERS
for r in ROUTERS:
    app.include_router(r, prefix=API_PREFIX)

from dotenv import load_dotenv
load_dotenv()
