from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from fastevents.db_connection import get_db
from datetime import datetime

from fastevents.models import Log
from fastevents.schemas.models import (
    LogCreate,
    LogRead,
    LogUpdate,    
)


def log_get_all(db: Session):
    return db.query(Log).all()

def log_get_one(db: Session , id : UUID):
    return db.query(Log).filter_by(id=id).one()

def log_create(db : Session , record : LogCreate):
    ts = datetime.now()
    db.add(Log(
        log_src = record.log_src,
        event_type = record.event_type,
        name = record.name,
        description = record.description,
        severity = record.severity,
        creation_date = ts,
    )
    )
    db.commit()
    return db.query(Log).filter_by(
        log_src = record.log_src,
        event_type = record.event_type,
        name = record.name,
        description = record.description,
        severity = record.severity,
        creation_date = ts,
        ).one()
