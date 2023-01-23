from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from fastevents.db_connection import get_db

from fastevents.models import Event
from fastevents.schemas.models import (
    LogCreate,
    LogRead,
    LogUpdate,   
)

from fastevents.utils.log_crud import (
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


@router.post("/create-log" , status_code=status.HTTP_201_CREATED)
def create_one(
    record : LogCreate,
    db : Session = Depends(get_db),
):
    return log_create(db=db , record=record)