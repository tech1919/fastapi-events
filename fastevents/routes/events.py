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
    event_create,
    event_delete,

)

router = APIRouter(tags=["Events"])

@router.get("/get-all-events" , status_code=status.HTTP_200_OK)
def get_all(
    db : Session = Depends(get_db),
):
    return event_get_all(db=db)


@router.get(
        "/get-one/{event_id}"
        )
async def get_one(
    event_id : UUID,
    db : Session = Depends(get_db),
):
    return event_get_one(db=db , id = event_id) 

@router.post(
        "/create"
)
async def create_one(
    record : EventCreate, 
    db : Session = Depends(get_db)
):
    return event_create(db=db , record=record)



@router.put(
    "/update/{event_id}",
)
async def update_one(
    event_id : UUID,
    update_fields : EventUpdate,
    db : Session = Depends(get_db),
):
    
    return event_update(db = db , record=update_fields , id = event_id)


@router.delete(
    "/delete/{event_id}"
)
async def delete_one(
    event_id : UUID,
    db : Session = Depends(get_db),
):
    return event_delete(db=db , id=event_id)
