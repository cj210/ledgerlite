# Standard imports
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

# Project imports
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate

# Initialize PasswordHash using Argon2 (recommended by OWASP)
password_hash = PasswordHash.recommended()


class UserService:

    def __init__(self, session: Session) -> None:
        self.session = session
        self.user_repo = UserRepository(session)

    def _hash_password(self, password: str) -> str:
        return password_hash.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return password_hash.verify(plain_password, hashed_password)

    def get_by_id(self, user_id: int) -> User:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID {user_id} not found",
            )
        return user

    def create_user(self, user_in: UserCreate) -> User:
        
        if self.user_repo.get_by_user_name(user_in.user_name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered",
            )
        if user_in.email and self.user_repo.get_by_email(user_in.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        if user_in.mobile and self.user_repo.get_by_mobile(user_in.mobile):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Mobile number already registered",
            )

        user_data = user_in.model_dump(exclude={"password"})
        hashed_password = self._hash_password(user_in.password)

        new_user = User(**user_data, password_hash=hashed_password)

        try:
            created_user = self.user_repo.create(new_user)
            self.session.commit()
            return created_user
        except Exception:
            self.session.rollback()
            raise
