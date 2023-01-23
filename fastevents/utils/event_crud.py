from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from fastevents.db_connection import get_db
from datetime import datetime

from fastevents.models import Event
from fastevents.schemas.models import (
    EventCreate,
    EventDelete,
    EventRead,
    EventUpdate,    
)

def event_get_all(db: Session):
    return db.query(Event).all()

def event_get_one(db: Session , id : UUID):
    return db.query(Event).filter_by(id=id).one()

def event_update(db: Session , record : EventUpdate):
    update_query = {
        Event.id : record.id ,
        Event.name : record.name,
        Event.content : record.content,
        Event.modify_date : datetime.now(),
        }
    db.query(Event).filter_by(id=record.id).update(update_query)
    db.commit()
    return db.query(Event).filter_by(id=record.id).one()