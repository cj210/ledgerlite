#Standard imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Project imports
from app.api.routes.user import user_router


ledger = FastAPI(title="Ledger Lite V1")
ledger.include_router(user_router, prefix="/api/v1")


ledger.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://192.168.29.56:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@ledger.get("/")
def landing_page():
    return {"Location": "Landing Page"}
