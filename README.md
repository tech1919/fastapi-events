# FastEvents - FastAPI Events System

This package is a ready to use user authentication and autorization managment system, Using FastAPI, PostgreSQL, and AWS Cognito JWT based authentication.
> ## Install Package

```
pip install "git+https://github.com/tech1919/fastapi-events.git"
```


> ## Configure Environment

Configure `.env` file:
```
USERS_DATABASE_URL=postgres://username:password@host:port/database_name
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



