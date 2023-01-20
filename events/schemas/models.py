from typing import Optional , List
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session


class BaseDelete:
    id : UUID
    message : str

########################
# Events               #
########################


class EventCreate(BaseModel):
    event_src : str 
    name : str
    content : dict

class EventUpdate(BaseModel):
    id : UUID
    name : str 
    content : dict

class EventDelete(BaseModel , BaseDelete):
    pass

class EventRead(BaseModel):
    id : UUID


########################
# Logs                 #
########################


class LogCreate(BaseModel):
    log_src : str 
    event_type : str
    name : str
    description : str
    severity : str

class LogUpdate(BaseModel):
    id : UUID
    name : str 

class LogRead(BaseModel):
    
    id : UUID
    source : str
    event_type : str
    name : str
    description : str
    severity : str
    creation_date : datetime
    