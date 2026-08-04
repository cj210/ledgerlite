# Standard imports
from fastapi import APIRouter, status
from datetime import datetime


# Project imports
from app.schemas.user import UserCreate, UserResponse
from app.domain.enums import UserType


user_router = APIRouter()




@user_router.post("/users", response_model = UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):

    response = UserResponse(
            **user.model_dump(exclude={"password"}),
            id = 1, 
            created_at = datetime.now(),
            updated_at = datetime.now())
    print(type(user))
    print(user)
    print(user.username)
    print(type(response))
    print(response)
    print(response.username)
    return response
    

@user_router.get("/user", response_model = UserResponse)
def get_user():
    response = UserResponse(
            username = "Alice",
            display_name = "Al",
            user_type = UserType.INDIVIDUAL,
            id = 71, 
            created_at = datetime.now(),
            updated_at = datetime.now())
    return response


