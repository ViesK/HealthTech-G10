from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import API_PREFIX

app = FastAPI(title="Health API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get(f"{API_PREFIX}/health")
def health():
    return {"message": "ok"}
