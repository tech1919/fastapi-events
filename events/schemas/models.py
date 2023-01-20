from typing import Optional , List
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session


########################
# Events               #
########################


class EventCreate(BaseModel):
    pass

class EventUpdate(BaseModel):
    id : UUID
    name : str 
    content : dict

class EventDelete(BaseModel):
    pass
class EventRead(BaseModel):
    pass
