# Standard imports
from fastapi import FastAPI


# Project imports
from app.core.config import settings
from app.database.session import get_db
from app.api.routes.health import health_router
from app.api.routes.user import user_router


app = FastAPI(title=settings.app_name)
app.include_router(health_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {"status": "ok"}
