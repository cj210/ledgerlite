# Standard imports
import pytest
from pydantic import ValidationError
from random import randint
from datetime import datetime


# Project imports
from app.schemas.user import UserBase, UserCreate, UserUpdate, UserResponse
from app.tests.generators.strings import random_string
from app.tests.factories.user import (
        make_base_user_data,
        make_create_user_data,
        )


class TestUserBase:

    @pytest.mark.parametrize("user_type_value", ["individual", "business"])
    def test_user_base_with_valid_user_details(self, user_type_value):

        test_data = make_base_user_data(user_type=user_type_value)

        result = UserBase(**test_data)

        assert result.user_name == test_data.get("user_name")
        assert result.display_name == test_data.get("display_name")
        assert result.user_type == test_data.get("user_type")
        assert result.description == test_data.get("description")
        assert result.email == test_data.get("email")
        assert result.mobile == test_data.get("mobile")

    @pytest.mark.parametrize("user_type_value", ["individual", "business"])
    def test_user_base_with_valid_user_details_including_underscore(self, user_type_value):

        test_data = make_base_user_data(user_type=user_type_value)
        test_data["user_name"] = test_data["user_name"][:-1] + "_"
        result = UserBase(**test_data)

        assert result.user_name == test_data.get("user_name")
        assert result.display_name == test_data.get("display_name")
        assert result.user_type == test_data.get("user_type")
        assert result.description == test_data.get("description")
        assert result.email == test_data.get("email")
        assert result.mobile == test_data.get("mobile")

    @pytest.mark.parametrize("user_name_length", [-1,0,2])
    def test_user_base_with_invalid_user_name_lengths_below_3(self, user_name_length):
        invalid_user_name = random_string(string_length=user_name_length, use_special=False)
        test_data = make_base_user_data(user_name=invalid_user_name, user_type="business")

        with pytest.raises(ValidationError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "user_name"
        assert error["type"] == "string_too_short"

    @pytest.mark.parametrize("key_value,max_length",
                             [
                                 ("user_name", 20),
                                 ("display_name", 30),
                                 ("description", 150),
                                 ]
                             )

    def test_user_base_with_invalid_key_values_above_permitted(self, key_value, max_length):
        invalid_value = randint(max_length+1,200)
        invalid_key_value = random_string(string_length=invalid_value, use_special=False)
        test_data = make_base_user_data(user_type="business")
        test_data[key_value] = invalid_key_value

        with pytest.raises(ValidationError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == key_value
        assert error["type"] == "string_too_long"

    def test_user_base_with_invalid_user_that_include_special_charectors(self):
        length_value= randint(3,20)
        invalid_user_name = random_string(string_length=length_value, use_special=True)[:-1] + "*"
        test_data = make_base_user_data(user_name=invalid_user_name, user_type='individual')

        with pytest.raises(ValidationError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "user_name"
        assert error["type"] == 'string_pattern_mismatch'

    @pytest.mark.parametrize("key_value,expected_type", 
                              [("user_name","string_type"),
                               ("display_name","string_type"),
                               ("user_type", "enum"),
                               ])
    def test_user_base_with_invalid_user_as_none(self, key_value, expected_type):
        test_data = make_base_user_data(user_type='individual')
        test_data[key_value] = None

        with pytest.raises(ValidationError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == key_value
        assert error["type"] == expected_type

    @pytest.mark.parametrize("display_name_length", [-1,0])
    def test_user_base_with_invalid_display_name_lengths_below_1(self, display_name_length):
        invalid_display_name = random_string(string_length=display_name_length)
        test_data = make_base_user_data(display_name=invalid_display_name, user_type="business")

        with pytest.raises(ValidationError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "display_name"
        assert error["type"] == "string_too_short"

    def test_user_base_with_invalid_user_type(self):
        test_data = make_base_user_data()

        with pytest.raises(ValidationError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "user_type"
        assert error["type"] == "enum"
    
    @pytest.mark.parametrize("key_value", ["description", "email", "mobile"])
    def test_user_base_for_valid_none_values(self, key_value):
        test_data = make_base_user_data(user_type='business')
        test_data[key_value] = None

        result = UserBase(**test_data)

        assert result.description == test_data.get("description")
        assert result.email == test_data.get("email")
        assert result.mobile == test_data.get("mobile")


    def test_user_base_for_invalid_email_format(self):

        invalid_email = random_string(string_length = 25, use_special=False)
        test_data = make_base_user_data(user_type='individual')
        test_data["email"] = invalid_email

        with pytest.raises(ValueError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "email"
        assert error["type"] == "value_error"



    def test_user_base_for_invalid_email_length(self):
        invalid_email = random_string(string_length=255, use_special=False) + "@example.com"
        test_data = make_base_user_data(user_type='business')
        test_data["email"] = invalid_email

        with pytest.raises(ValidationError) as exc_info:
            UserBase(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "email"
        assert error["type"] == "value_error"


    def test_user_base_for_invalid_mobile_format(self):
        invalid_mobile = random_string(string_length=9) + '%'

        test_data = make_base_user_data(user_type="business")
        test_data["mobile"] = invalid_mobile

        with pytest.raises(ValueError) as exc_info:
            UserBase(**test_data)
        
        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "mobile"
        assert error["type"] == "string_pattern_mismatch"


class TestUserCreate:

    def test_user_create_for_valid_data(self):

        test_data = make_create_user_data(user_type='individual')

        result = UserCreate(**test_data)

        assert result.password == test_data["password"]

    @pytest.mark.parametrize("password_length, error_type",
                             [
                                 (2,"string_too_short"),
                                 (0,"string_too_short"),
                                 (100,"string_too_long")
                                 ]
                             )
    def test_user_create_for_invalid_password(self, password_length, error_type):
        invalid_password = random_string(string_length=password_length)
        test_data = make_create_user_data(user_type='business')
        test_data["password"] = invalid_password

        with pytest.raises(ValidationError) as exc_info:
            UserCreate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "password"
        assert error["type"] == error_type

    def test_user_create_for_invalid_password_none(self):
        test_data = make_create_user_data(user_type='individual')
        test_data["password"] = None

        with pytest.raises(ValidationError) as exc_info:
            UserCreate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "password"
        assert error["type"] == "string_type"


class TestUserUpdate:

    def test_user_update_with_valid_data(self):

        test_data = make_base_user_data(user_type='individual')

        result = UserUpdate(**test_data)

        assert result.display_name == test_data.get("display_name")
        assert result.description == test_data.get("description")
        assert result.user_type == test_data.get("user_type")
        assert result.email == test_data.get("email")
        assert result.mobile == test_data.get("mobile")

    @pytest.mark.parametrize("key_value",["display_name", "user_type", "description", "email", "mobile"])
    def test_user_update_for_each_key_as_none(self, key_value):

        test_data = make_base_user_data(user_type='business')
        test_data[key_value] = None

        result = UserUpdate(**test_data)

        assert result.display_name == test_data.get("display_name")
        assert result.description == test_data.get("description")
        assert result.user_type == test_data.get("user_type")
        assert result.email == test_data.get("email")
        assert result.mobile == test_data.get("mobile")

    @pytest.mark.parametrize("key_value,boundary,error_type",
                             [
                                 ("display_name", -1, "string_too_short"),
                                 ("display_name", 0, "string_too_short"),
                                 ("display_name", 55, "string_too_long"),
                                 ("description", 255, "string_too_long"),
                                 ]
                             )
    def test_user_update_for_invalid_display_name_and_description_boundaries(self, key_value,boundary,error_type):

        test_data = make_base_user_data(user_type="individual")
        test_data[key_value] = random_string(string_length=boundary)

        with pytest.raises(ValidationError) as exc_info:
            UserUpdate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == key_value
        assert error['type'] == error_type

    def test_user_update_for_invalid_user_type(self):

        test_data = make_base_user_data()

        with pytest.raises(ValidationError) as exc_info:
            UserUpdate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "user_type"
        assert error["type"] == "enum"

    def test_user_update_for_invalid_email_length(self):

        invalid_email = random_string(string_length=255, use_special=False) + "ding.com"
        test_data = make_base_user_data(user_type='business')
        test_data["email"] = invalid_email

        with pytest.raises(ValueError) as exc_info:
            UserUpdate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "email"
        assert error["type"] == "value_error"


    def test_user_update_for_invalid_email_format(self):

        invalid_email = random_string(string_length=55, use_special=False) 
        test_data = make_base_user_data(user_type='business')
        test_data["email"] = invalid_email

        with pytest.raises(ValueError) as exc_info:
            UserUpdate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "email"
        assert error["type"] == "value_error"

    def test_user_update_for_invalid_mobile_format(self):

        invalid_mobile = random_string(string_length=9) + '*'
        test_data = make_base_user_data(user_type="business")
        test_data["mobile"] = invalid_mobile

        with pytest.raises(ValidationError) as exc_info:
            UserUpdate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "mobile"
        assert error["type"] == "string_pattern_mismatch"

    def test_user_update_for_invalid_mobile_length(self):

        invalid_mobile = random_string(string_length=19) 
        test_data = make_base_user_data(user_type="business")
        test_data["mobile"] = invalid_mobile

        with pytest.raises(ValidationError) as exc_info:
            UserUpdate(**test_data)

        errors = exc_info.value.errors()
        error = errors[0]

        assert len(errors) == 1
        assert error["loc"][0] == "mobile"
        assert error["type"] == "string_pattern_mismatch"


class TestUserResponse:

    def test_user_response_validates_from_object_attributes(self, mocker):

        mock_values = make_base_user_data(user_type="individual")
        mock_response_object = mocker.Mock(**mock_values, id = 5, created_at = datetime.now(), updated_at=datetime.now())
        
        result = UserResponse.model_validate(mock_response_object)

        assert result.id == 5
        assert result.user_name == mock_response_object.user_name
        assert result.display_name == mock_response_object.display_name
        assert result.user_type == mock_response_object.user_type
        assert result.description == mock_response_object.description
        assert result.email == mock_response_object.email
        assert result.mobile == mock_response_object.mobile
        assert result.created_at == mock_response_object.created_at
        assert result.updated_at == mock_response_object.updated_at





        



