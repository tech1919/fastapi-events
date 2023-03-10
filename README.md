# FastEvents - FastAPI Events System

This package is a ready to use event syste, Using FastAPI, PostgreSQL.
> ## Install Package

```
pip install "git+https://github.com/tech1919/fastapi-events.git"
```


> ## Configure Environment

Configure `.env` file:
```
EVENTS_DATABASE_URL=postgresql://username:password@host:port/database_name
```

> ## Add the router to your FastAPI app

import:
```python
from fastevents.router import events_router
from fastapi import FastAPI
```

define the app:
```python
app = FastAPI(
    title = "API's name"
)
```

include the router:
```python
app.include_router(router = events_router , prefix="/notif")
```



