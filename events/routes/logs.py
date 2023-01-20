from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from events.db_connection import get_db

from events.models import Event
from events.schemas.models import (
    LogCreate,
    LogRead,
    LogUpdate,   
)

from events.utils.log_crud import (
    log_create,
    log_get_all,
    log_get_one,
)



router = APIRouter(tags=["Logs"])

@router.get("/get-all-logs" , status_code=status.HTTP_200_OK)
def get_all(
    db : Session = Depends(get_db),
):
    return log_get_all(db=db)


@router.post("/create-log" , status_code=status.HTTP_201_OK)
def create_one(
    record : LogCreate,
    db : Session = Depends(get_db),
):
    return log_create(db=db , record=record)