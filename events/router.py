from fastapi import APIRouter , Depends

from events.routes import (
    events,
    logs,
)

events_router = APIRouter()

events_router.include_router( router = events.router , prefix="/events")
events_router.include_router( router = logs.router , prefix="/logs")