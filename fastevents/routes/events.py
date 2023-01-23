from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from fastevents.db_connection import get_db

from fastevents.models import Event
from fastevents.schemas.models import (
    EventCreate,
    EventDelete,
    EventRead,
    EventUpdate,
)

from fastevents.utils.event_crud import (
    event_get_all,
    event_get_one,
    event_update,
)

router = APIRouter(tags=["Events"])

@router.get("/get-all-events" , status_code=status.HTTP_200_OK)
def get_all(
    db : Session = Depends(get_db),
):
    return event_get_all(db=db)