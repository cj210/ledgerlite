# Standard imports
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

# Project imports
from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
) -> UserResponse:
    user_service = UserService(session=db)
    return user_service.create_user(user_in)


@user_router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Get user by ID",
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
) -> UserResponse:
    user_service = UserService(session=db)
    return user_service.get_by_id(user_id)
