import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String , ForeignKey , Integer , JSON , Boolean , DateTime
from sqlalchemy.dialects.postgresql import UUID

from typing import AsyncGenerator
from datetime import datetime
from .db_connection import Base, engine


class Event(Base):

    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    event_src = Column(String , nullable = False)
    event_type = Column(String , nullable = False)
    event_subtype = Column(String , nullable = True)
    name = Column(String(100) , nullable=False)
    content = Column(String , nullable=False)
    severity = Column(String(50) , nullable = True)
    creation_date = Column(DateTime , default = datetime.now())
    modify_date = Column(DateTime , default = datetime.now())
    attachments = Column(JSON , nullable = True)
    parent_event_id = Column(UUID(as_uuid=True) , ForeignKey("events.id") ,nullable = True)


class Log(Base):

    __tablename__ = "logs"
    
    id = Column(UUID(as_uuid=True), primary_key=True , default = uuid.uuid4)
    log_src = Column(String , nullable = False)
    event_type = Column(String(50))
    name = Column(String(100) , nullable=True)
    description = Column(String , nullable=False)
    severity = Column(String(50))
    creation_date = Column(DateTime , default = datetime.now())
    


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
