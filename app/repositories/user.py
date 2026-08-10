# Standard imports
import inspect
from sqlalchemy import select
from sqlalchemy.orm import Session

# Project imports
from app.models.user import UserModel


class UserRepository:

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, id: int) -> UserModel | None:
        """Fetch a single user model by primary key ID."""
        return self.session.get(UserModel, id)

    def get_by_user_name(self, user_name: str) -> UserModel | None:
        """Fetch a user model by unique username."""
        stmt = select(UserModel).where(UserModel.user_name == user_name)
        return self.session.scalars(stmt).first()

    def get_by_email(self, email: str) -> UserModel | None:
        """Fetch a user model by unique email address."""
        stmt = select(UserModel).where(UserModel.email == email)
        return self.session.scalars(stmt).first()

    def get_by_mobile(self, mobile: str) -> UserModel | None:
        """Fetch a user model by unique mobile number."""
        stmt = select(UserModel).where(UserModel.mobile == mobile)
        return self.session.scalars(stmt).first()

    def create(self, user_in: UserModel) -> UserModel:
        """Add, flush, and refresh a new user model in the database session."""
        self.session.add(user_in)
        self.session.flush()
        self.session.refresh(user_in)
        return user_in

    def _get_methods_directory(self) -> dict[str, str]:
        """Extract public methods and their docstrings dynamically."""
        methods = {}
        for name, func in inspect.getmembers(self, predicate=inspect.ismethod):
            if not name.startswith("_"):
                # Clean up whitespace from multi-line or indented docstrings
                doc = inspect.getdoc(func) or "No description provided."
                methods[name] = doc
        return methods

    def __repr__(self) -> str:
        return f"<UserRepository methods={self._get_methods_directory()}>"

    def __str__(self) -> str:
        return str(self._get_methods_directory())
