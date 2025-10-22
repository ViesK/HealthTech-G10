from fastapi import APIRouter, Depends, Header, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.db import get_db
from app.modules.notifications.model import Notification
from app.modules.notifications.schema import NotificationCreate, NotificationRead, NotificationUpdate
from app.modules.notifications import service



router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post("", response_model=NotificationRead, status_code=status.HTTP_201_CREATED)
def create_notification(
        payload: NotificationCreate, 
        send: bool = Query(True, description="Enviar inmediatamente"), 
        db: Session = Depends(get_db)
    ):
    try:
        return service.create_notification(db, payload, send_now=send)
    except Exception as e:
        # En MVP cualquier fallo interno devuelve 500
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{notification_id}", response_model=NotificationRead)
def read_notification(notification_id: int, db: Session = Depends(get_db)):
    try:
        return service.read_notification(db, notification_id)
    except service.NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{notification_id}", response_model=NotificationRead)
def update_notification(notification_id: int, payload: NotificationUpdate, db: Session = Depends(get_db)):
    try:
        return service.update_notification(db, notification_id, payload)
    except service.NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
