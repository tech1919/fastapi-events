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

class S3File(BaseModel):

    file_ext : str
    s3_uri : str

class Attachments(BaseModel):

    files : List[S3File]

class EventCreate(BaseModel):
    event_src : str
    event_type : str
    event_subtype : Optional[str] = None
    name : str
    content : str
    severity : str
    creation_date : datetime
    modify_date : datetime
    attachments : Attachments
    parent_event_id : Optional[UUID] = None

class EventUpdate(BaseModel):

    event_src : Optional[str] = None
    event_type : Optional[str] = None
    event_subtype : Optional[str] = None
    name : Optional[str] = None
    content : Optional[str] = None
    severity : Optional[str] = None
    modify_date : Optional[datetime] = None
    attachments : Optional[Attachments] = None
    parent_event_id : Optional[UUID] = None


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
    