# Standad imports
import pytest
from random import randint


# Project imports
from app.api.routes.user import create_user, get_user
from app.tests.factories.user import make_create_user_data

class TestCreateUser:

    def test_create_user_for_user_service_called_and_user_create_returns(self, mocker):

        mock_user_in = make_create_user_data(user_type='business')
        mock_session = mocker.Mock()
        mock_user_service = mocker.Mock()
        mock_user_service.create_user.return_value = "Success"
        mock_user_service_class = mocker.patch("app.api.routes.user.UserService", return_value=mock_user_service)

        result = create_user(mock_user_in, db=mock_session)

        mock_user_service_class.assert_called_once_with(session=mock_session)
        mock_user_service.create_user.assert_called_once_with(mock_user_in)
        assert result == "Success"

    def test_get_user_for_user_service_called_and_get_by_id_returns(self, mocker):

        mock_user_id = randint(1,99)
        mock_session = mocker.Mock()
        mock_user_service = mocker.Mock()
        mock_user_service.get_by_id.return_value = "Success"
        mock_user_service_class = mocker.patch("app.api.routes.user.UserService", return_value=mock_user_service)

        result = get_user(user_id=mock_user_id, db=mock_session)

        mock_user_service_class.assert_called_once_with(session=mock_session)
        mock_user_service.get_by_id.assert_called_once_with(mock_user_id)
        assert result == "Success"
        
        

