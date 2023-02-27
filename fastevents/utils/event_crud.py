from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from fastevents.db_connection import get_db
from datetime import datetime
import json

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

def event_update(db: Session , record : EventUpdate , id = UUID):
    
    update_query = {}
    for key in record.dict().keys():
        if record.dict()[key] != None:
            update_query[key] = record.dict()[key]
        
    db.query(Event).filter_by(id=id).update(update_query)
    db.commit()

    return event_get_one(db=db , id = id)

def event_create(db : Session , record : EventCreate):

    

    new_event = Event(
        event_src = record.event_src,
        event_type = record.event_type,
        event_subtype = record.event_subtype,
        name = record.name,
        content = record.content,
        severity = record.severity,
        creation_date = record.creation_date,
        modify_date = record.modify_date,
        attachments = record.attachments.dict(),
        parent_event_id = record.parent_event_id,
    )

    db.add(new_event)
    db.commit()

    return db.query(Event).filter_by(
        event_src = record.event_src,
        event_type = record.event_type,
        event_subtype = record.event_subtype,
        name = record.name,
        content = record.content,
        severity = record.severity,
        creation_date = record.creation_date,
        modify_date = record.modify_date 
    ).first()

def event_delete(db: Session , id : UUID):

    db.query(Event).filter_by(id = id).delete()
    db.commit()

    return {"msg" : f"Record {id} deleted"}