from fastapi import FastAPI
from app.core.config import settings
from app.database.session import get_db
from app.api.routes.health import health_router


app = FastAPI(title=settings.app_name)
app.include_router(health_router)


@app.get("/")
def root():
    return {"status": "ok", "bisket": "cutlet", "type": f'{type(43)}'}
