# Standar_imports
from random import randint

# Project imports
from app.tests.generators.strings import email, mobile_string, random_string


def make_update_user_data(**overrides) -> dict:
    """Returns a raw dictionary of UserUpdate"""
    length = randint(1,30)
    data = {
        "display_name": random_string(string_length=length),
        "user_type": "DUMMY_TYPE_STRING",
        "description": random_string(150),
        "email": email(),
        "mobile": mobile_string(10),
    }

    data.update(overrides)
    return data 


def make_base_user_data(**overrides) -> dict:
    """Returns a raw dictionary of Userbase data."""
    data = make_update_user_data()
    length = randint(3,20)
    data["user_name"] = random_string(string_length=length, use_special=False)
    
    data.update(overrides)
    return data


def make_create_user_data(**overrides) -> dict:
    """Returns a raw dictionary of UserCreate data."""
    data = make_base_user_data()
    length = randint(8,20)
    data["password"] = random_string(string_length=length)

    data.update(overrides)
    return data


def make_repo_user_data(**overrides) -> dict:
    """Returns a raw dictionary of UserRepository data."""
    data = make_create_user_data()
    data["password_hash"] = data.pop("password")

    data.update(overrides)
    return data


def make_model_user_data(**overrides) -> dict:
    "Adds status key to make UserModel data"
    data = make_repo_user_data()
    data["status"] = "Active"
    data.update(overrides)
    return data
