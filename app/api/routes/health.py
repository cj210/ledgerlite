from fastapi import APIRouter
from app.core.config import settings

health_router = APIRouter()

@health_router.get("/health")
def get_health():
    return { "Name": settings.app_name,
             "DB": settings.database_name,
             "Debug": settings.debug }

