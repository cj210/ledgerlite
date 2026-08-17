# Standard imports
import pytest

# Project imports
from app.models.user import User
from app.tests.factories.user import make_repo_user_data
from app.tests.generators.strings import random_string


class TestUser:

    def test_user_model_with_valid_data(self):

        class MockUserType:
            def __str__(self) -> str:
                return "CUSTOM_TYPE"

        data = make_repo_user_data()
        data["user_type"] = MockUserType()

        user = User(**data)

        assert user.user_name == data["user_name"]
        assert user.display_name == data["display_name"]
        assert user.password_hash == data["password_hash"]
        assert str(user.user_type) == "CUSTOM_TYPE"
        assert user.description == data["description"]
        assert user.email == data["email"]
        assert user.mobile == data["mobile"]
        assert user.status == None

        assert repr(user) == (
            f"<User(Table Name: users Record: id={user.id}, "
            f"user_name='{user.user_name}', "
            f"user_type='{user.user_type}')>"
        )

        assert str(user) == f"{user.display_name} (@{user.user_name})"

    @pytest.mark.parametrize(
    "optional_fields",
    [
        {"description": None},
        {"email": None},
        {"mobile": None},
        {
            "description": None,
            "email": None,
            "mobile": None,
        },
    ],
    )
    def test_user_model_accepts_none_for_optional_fields(self, optional_fields):
        class MockUserType:
            def __str__(self) -> str:
                return "CUSTOM_TYPE"

        data = make_repo_user_data()
        data["user_type"] = MockUserType()
        data.update(optional_fields)

        user = User(**data)

        assert user.status == None
        for field, expected_value in optional_fields.items():
            assert getattr(user, field) is expected_value

    @pytest.mark.parametrize(
    "field",
    [
        "user_name",
        "display_name",
        "password_hash",
        "user_type",
    ],
    )
    def test_user_model_required_fields_can_be_set_to_none(self, field):
        class MockUserType:
            def __str__(self) -> str:
                return "CUSTOM_TYPE"

        data = make_repo_user_data()
        data["user_type"] = MockUserType()
        data[field] = None

        user = User(**data)

        assert user.status == None
        assert getattr(user, field) is None


    @pytest.mark.parametrize(
    "field",
    [
        "user_name",
        "display_name",
        "password_hash",
        "user_type",
    ],
    )
    def test_user_model_missing_required_field(self, field):
        data = make_repo_user_data()
        data.pop(field)

        user = User(**data)

        assert user.status == None
        assert getattr(user, field) is None


    @pytest.mark.parametrize(
    "field",
    [
        "description",
        "email",
        "mobile",
    ],
    )
    def test_user_model_missing_optional_field(self, field):
        data = make_repo_user_data()
        data.pop(field)

        user = User(**data)

        assert user.status == None
        assert getattr(user, field) is None

    @pytest.mark.parametrize(
    "field,length",
    [
        ("user_name", 21),
        ("display_name", 31),
        ("password_hash", 129),
        ("description", 151),
        ("email", 256),
        ("mobile", 11),
    ],
    )
    def test_user_model_accepts_over_length_string(self, field, length):
        data = make_repo_user_data()
        data[field] = random_string(length)

        user = User(**data)

        assert user.status == None
        assert getattr(user, field) == data[field]
