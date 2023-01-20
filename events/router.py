from fastapi import APIRouter , Depends

from events.routes import (
    events
)

events_router = APIRouter()

events_router.include_router( router = events.router , prefix="/events")