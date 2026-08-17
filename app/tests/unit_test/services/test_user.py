# Standard imports
import pytest
import random
from fastapi import HTTPException


# Project imports
from app.services.user import UserService
from app.tests.factories.user import make_create_user_data



class TestInitUserService:

    def test_user_service_initialization(self, mocker):

        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        user_repo = mocker.patch("app.services.user.UserRepository", return_value= mock_user_repo)
        
        result = UserService(session)

        user_repo.assert_called_once_with(session)
        assert result.session is session
        assert result.user_repo is mock_user_repo


class TestHashPassword:

    def test_password_hash_return_hashed_password(self, mocker):

        pwd = "12345"
        session = mocker.Mock()
        mock_hash_password = mocker.Mock()
        mock_hash_password.hash.return_value = pwd
        mocker.patch("app.services.user.password_hash", mock_hash_password)

        user_service = UserService(session)
        result = user_service._hash_password(pwd)

        assert result == pwd
        mock_hash_password.hash.assert_called_once_with(pwd)

class TestVerifyPassword:

    @pytest.mark.parametrize("verification_value", [True, False])
    def test_verify_password_returns_verification_result(self, verification_value, mocker):

        session = mocker.Mock()
        mock_password_hash = mocker.Mock()
        mock_password_hash.verify.return_value = verification_value
        mocker.patch("app.services.user.password_hash", mock_password_hash)

        user_service = UserService(session)
        result = user_service.verify_password("123", "456")

        mock_password_hash.verify.assert_called_once_with("123", "456")
        assert result is verification_value

class TestGetById:

    def test_get_user_by_valid_user_id(self, mocker):

        dummy_id = random.randint(1,999)
        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        mock_user_model = mocker.Mock()
        mock_user_repo.get_by_id.return_value = mock_user_model
        mocker.patch("app.services.user.UserRepository", return_value = mock_user_repo)

        user_service = UserService(session)
        result = user_service.get_by_id(dummy_id)

        mock_user_repo.get_by_id.assert_called_once_with(dummy_id)
        assert result is mock_user_model

    def test_get_user_by_invalid_user_id(self, mocker):

        dummy_id = random.randint(1,999)
        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        mock_user_repo.get_by_id.return_value = None
        mocker.patch("app.services.user.UserRepository", return_value = mock_user_repo)

        user_service = UserService(session)
        with pytest.raises(HTTPException) as exc_info:
            user_service.get_by_id(dummy_id)

        mock_user_repo.get_by_id.assert_called_once_with(dummy_id)
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == f"User with ID {dummy_id} not found"


class TestCreateUser:

    def test_create_user_with_valid_data(self, mocker):

        mock_password_hash_value = "Random"
        raw_user_data = make_create_user_data()
        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        mock_user_create = mocker.Mock(**raw_user_data, model_dump=mocker.Mock(return_value=raw_user_data))
        mocker.patch("app.services.user.UserRepository", return_value=mock_user_repo)
        mock_user_repo.get_by_mobile.return_value = None
        mock_user_repo.get_by_email.return_value = None 
        mock_user_repo.get_by_user_name.return_value = None
        mock_hash_password_method = mocker.patch("app.services.user.UserService._hash_password", return_value=mock_password_hash_value)
        mock_user_class = mocker.patch("app.services.user.User", return_value=mock_user_create)
        mock_user_repo.create.return_value = mock_user_create

        user_service = UserService(session)
        result = user_service.create_user(mock_user_create)

        mock_user_repo.get_by_mobile.assert_called_once_with(mock_user_create.mobile)
        # mock_user_repo.get_by_email.return_value = None 
        # mock_user_repo.get_by_user_name.return_value = None
        mock_user_repo.get_by_user_name.assert_called_once_with(mock_user_create.user_name)
        mock_hash_password_method.assert_called_once_with(mock_user_create.password)
        mock_user_class.assert_called_once_with(**raw_user_data, password_hash=mock_password_hash_value)
        mock_user_repo.create.assert_called_once_with(mock_user_create)
        user_service.session.commit.assert_called_once()
        assert result is mock_user_create

    def test_create_user_failure_with_exception(self, mocker):

        mock_password_hash_value = "Random"
        raw_user_data = make_create_user_data()
        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        mock_user_create = mocker.Mock(**raw_user_data, model_dump=mocker.Mock(return_value=raw_user_data))
        mocker.patch("app.services.user.UserRepository", return_value=mock_user_repo)
        mock_user_repo.get_by_mobile.return_value = None
        mock_user_repo.get_by_email.return_value = None 
        mock_user_repo.get_by_user_name.return_value = None
        mock_hash_password_method = mocker.patch("app.services.user.UserService._hash_password", return_value=mock_password_hash_value)
        mock_user_class = mocker.patch("app.services.user.User", return_value=mock_user_create)
        mock_user_repo.create.side_effect = Exception("Database connection failed")

        user_service = UserService(session)
        with pytest.raises(Exception, match="Database connection failed"):
            user_service.create_user(mock_user_create)
        user_service.session.rollback.assert_called_once()


    def test_existing_user_name_raises_exception(self, mocker):

        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        mock_user_create = mocker.Mock()
        mocker.patch("app.services.user.UserRepository", return_value=mock_user_repo)
        mock_user_repo.get_by_user_name.return_value = "Random"

        user_service = UserService(session)
        with pytest.raises(HTTPException) as exc_info:
            user_service.create_user(mock_user_create)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Username already registered"

    def test_existing_email_raises_exception(self, mocker):

        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        mock_user_create = mocker.Mock()
        mocker.patch("app.services.user.UserRepository", return_value=mock_user_repo)
        mock_user_repo.get_by_email.return_value = "Random"
        mock_user_repo.get_by_user_name.return_value = None

        user_service = UserService(session)
        with pytest.raises(HTTPException) as exc_info:
            user_service.create_user(mock_user_create)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Email already registered"

    def test_existing_mobile_raises_exception(self, mocker):

        session = mocker.Mock()
        mock_user_repo = mocker.Mock()
        mock_user_create = mocker.Mock()
        mocker.patch("app.services.user.UserRepository", return_value=mock_user_repo)
        mock_user_repo.get_by_mobile.return_value = "Random"
        mock_user_repo.get_by_email.return_value = None 
        mock_user_repo.get_by_user_name.return_value = None

        user_service = UserService(session)
        with pytest.raises(HTTPException) as exc_info:
            user_service.create_user(mock_user_create)

        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "Mobile number already registered"

