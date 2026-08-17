# Standard imports
import random
import pytest

# Project imports
from app.models.user import User
from app.repositories.user import UserRepository
from app.tests.factories.user import make_model_user_data


class TestUserRepositoryRepresentation:

    def test_repr(self, mocker):
        session = mocker.Mock()
        repository = UserRepository(session)

        result = repr(repository)

        assert result.startswith("<UserRepository methods=")
        assert "get_by_id" in result
        assert "get_by_user_name" in result
        assert "get_by_email" in result
        assert "get_by_mobile" in result
        assert "create" in result

    def test_str(self, mocker):
        session = mocker.Mock()
        repository = UserRepository(session)

        result = str(repository)

        assert "get_by_id" in result
        assert "get_by_user_name" in result
        assert "get_by_email" in result
        assert "get_by_mobile" in result
        assert "create" in result


class TestGetByIdUserRepository:

    def test_get_by_id_returns_user(self, mocker):
        user_id = random.randint(1, 9999)

        expected_user = User(**make_model_user_data())

        session = mocker.Mock()
        session.get.return_value = expected_user

        repository = UserRepository(session)

        result = repository.get_by_id(user_id)

        session.get.assert_called_once_with(User, user_id)
        assert result is expected_user

    def test_get_by_id_returns_none_when_user_not_found(self, mocker):
        user_id = random.randint(1, 9999)

        session = mocker.Mock()
        session.get.return_value = None

        repository = UserRepository(session)

        result = repository.get_by_id(user_id)

        session.get.assert_called_once_with(User, user_id)
        assert result is None

class TestUserRepositoryLookup:

    @pytest.mark.parametrize(
        "method_name, field_name",
        [
            ("get_by_user_name", "user_name"),
            ("get_by_email", "email"),
            ("get_by_mobile", "mobile"),
        ],
    )
    def test_lookup_returns_user(self, mocker, method_name, field_name):
        expected_user = User(**make_model_user_data())

        scalar_result = mocker.Mock()
        scalar_result.first.return_value = expected_user

        session = mocker.Mock()
        session.scalars.return_value = scalar_result

        repository = UserRepository(session)

        lookup_method = getattr(repository, method_name)
        result = lookup_method(getattr(expected_user, field_name))

        session.scalars.assert_called_once()

        statement = session.scalars.call_args.args[0]

        assert statement.whereclause.left.name == field_name
        assert statement.whereclause.right.value == getattr(
            expected_user,
            field_name,
        )

        scalar_result.first.assert_called_once_with()
        assert result is expected_user

    @pytest.mark.parametrize(
        "method_name, lookup_value",
        [
            ("get_by_user_name", "No_User"),
            ("get_by_email", "no_user@example.com"),
            ("get_by_mobile", "0000000000"),
        ],
    )
    def test_lookup_returns_none_when_user_not_found(
        self,
        mocker,
        method_name,
        lookup_value,
    ):
        scalar_result = mocker.Mock()
        scalar_result.first.return_value = None

        session = mocker.Mock()
        session.scalars.return_value = scalar_result

        repository = UserRepository(session)

        lookup_method = getattr(repository, method_name)
        result = lookup_method(lookup_value)

        session.scalars.assert_called_once()
        scalar_result.first.assert_called_once_with()

        assert result is None


class TestCreateUserRepository:

    def test_create_returns_user(self, mocker):
        user = User(**make_model_user_data())

        session = mocker.Mock()

        repository = UserRepository(session)

        result = repository.create(user)

        session.add.assert_called_once_with(user)
        session.flush.assert_called_once_with()
        session.refresh.assert_called_once_with(user)

        assert result is user

    def test_create_propagates_flush_exception(self, mocker):
        user = User(**make_model_user_data())

        session = mocker.Mock()
        session.flush.side_effect = RuntimeError("Database error")

        repository = UserRepository(session)

        with pytest.raises(RuntimeError, match="Database error"):
            repository.create(user)

        session.add.assert_called_once_with(user)
        session.flush.assert_called_once_with()
        session.refresh.assert_not_called()



