from .models import (
    Event
)
from .router import events_router
from fastevents.routes import (
    events,
    logs,
)

from fastevents.env_settings import *
from fastevents import env_settings