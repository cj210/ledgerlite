#Standard imports
from fastapi import FastAPI

# Project imports
from app.api.routes.user import user_router


ledger = FastAPI(title="Ledger Lite V1")
ledger.include_router(user_router, prefix="/api/v1")




@ledger.get("/")
def landing_page():
    return {"Location": "Landing Page"}
