# Standard imports
import pytest
from app.models.base import Base
from app.models.user import User
from app.repositories.user import UserRepository
from app.services.user import UserService
from app.schemas.user import UserCreate
from fastapi import HTTPException

# Project imports
from app.tests.factories.user import make_repo_user_data, make_create_user_data

class TestCreateUserIntegration:

    def test_test_database_has_user_table(self, test_db):

        tables = Base.metadata.tables

        assert "users" in tables

    def test_user_can_be_persisted(self, test_db):

        user_data = make_repo_user_data(user_type="individual")
        user = User(**user_data)

        test_db.add(user)
        test_db.commit()
        test_db.refresh(user)

        assert user.id is not None
        assert user.email == user_data["email"]
        assert user.user_name == user_data["user_name"]
        assert user.user_type == user_data["user_type"]
        assert user.display_name == user_data["display_name"]  
        assert user.description == user_data["description"]
        assert user.mobile == user_data["mobile"]
        assert user.password_hash == user_data["password_hash"]
        assert user.status == "active"
        assert user.created_at is not None
        assert user.updated_at is not None

    def test_user_repository_can_create_user(self, test_db):

        repo = UserRepository(test_db)
        user_data = make_repo_user_data(user_type="individual")
        user = User(**user_data)

        created_user = repo.create(user)
        
        assert created_user.id is not None
        assert created_user.user_name == user_data["user_name"]
        assert created_user.user_type == user_data["user_type"]
        assert created_user.display_name == user_data["display_name"]
        assert created_user.description == user_data["description"]
        assert created_user.email == user_data["email"]
        assert created_user.mobile == user_data["mobile"]
        assert created_user.password_hash == user_data["password_hash"] 
        assert created_user.status == "active"
        assert created_user.created_at is not None
        assert created_user.updated_at is not None

    def test_user_service_can_create_user(self, test_db):

        service = UserService(test_db)
        user_data = make_create_user_data(user_type="individual")
        user_create = UserCreate(**user_data)

        created_user = service.create_user(user_create)

        assert created_user.id is not None
        assert created_user.user_name == user_data["user_name"]
        assert created_user.password_hash is not None
        assert created_user.password_hash != user_data["password"]  
        assert created_user.user_type == user_data["user_type"]
        assert created_user.display_name == user_data["display_name"]
        assert created_user.description == user_data["description"]
        assert created_user.email == user_data["email"]
        assert created_user.mobile == user_data["mobile"]
        assert created_user.status == "active"
        assert created_user.created_at is not None
        assert created_user.updated_at is not None

        stored_user = test_db.query(User).filter( User.id == created_user.id).first()
        assert stored_user is not None
    
    @pytest.mark.parametrize("key_value,msg", [
        ("user_name", "Username already registered"),
        ("email", "Email already registered"),
        ("mobile", "Mobile number already registered")
    ])
    def test_user_rejects_duplicate_fields(self, test_db, key_value, msg):

        service = UserService(test_db)
        user_data = make_create_user_data(user_type="individual")
        user_create = UserCreate(**user_data)
        service.create_user(user_create)
        user_data_duplicate = make_create_user_data(user_type="individual", **{key_value: user_data[key_value]})
        user_create_duplicate = UserCreate(**user_data_duplicate)
         
        with pytest.raises(HTTPException) as exc_info:
            service.create_user(user_create_duplicate)
        
        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == msg

class TestGetByIdUserIntegration:

    def test_user_service_can_get_user_by_id(self, test_db):

        service = UserService(test_db)
        user_data = make_create_user_data(user_type="individual")
        user_create = UserCreate(**user_data)

        created_user = service.create_user(user_create)

        fetched_user = service.get_by_id(created_user.id)

        assert fetched_user is not None
        assert fetched_user.id == created_user.id
        assert fetched_user.user_name == created_user.user_name
        assert fetched_user.display_name == created_user.display_name
        assert fetched_user.description == created_user.description
        assert fetched_user.user_type == created_user.user_type
        assert fetched_user.email == created_user.email
        assert fetched_user.mobile == created_user.mobile
        assert fetched_user.status == created_user.status
        assert fetched_user.created_at == created_user.created_at
        assert fetched_user.updated_at == created_user.updated_at
        
    def test_user_service_returns_none_for_nonexistent_id(self, test_db):

        service = UserService(test_db)
        non_existent_id = 9999

        with pytest.raises(HTTPException) as exc_info:
            service.get_by_id(non_existent_id)  
        
        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == f"User with ID {non_existent_id} not found"

class TestHTTPUserIntegration:

    def test_user_end_point_works(self, client):
        
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"Location": "Landing Page"}
    
    def test_user_is_created_via_api(self, client):

        user_data = make_create_user_data(user_type="individual")

        response = client.post("/api/v1/users/", json=user_data)

        response_data = response.json()
        
        assert response.status_code == 201
        assert response_data["id"] is not None
        assert response_data["user_name"] == user_data["user_name" ]
        assert response_data["email"] == user_data["email"]
        assert response_data["mobile"] == user_data["mobile"]
        assert response_data["display_name"] == user_data["display_name"]
        assert response_data["description"] == user_data["description"]
        assert response_data["user_type"] == user_data["user_type"]
        assert response_data["created_at"] is not None
        assert response_data["updated_at"] is not None
        assert response_data.get("password") is None
        assert response_data.get("password_hash") is None
        assert response_data.get("status") == None
    
    @pytest.mark.parametrize("key_value,msg", [
        ("user_name", "Username already registered"),
        ("email", "Email already registered"),
        ("mobile", "Mobile number already registered")
    ])  
    def test_duplicate_user_is_rejected_via_api(self, client, key_value, msg):

        user_data = make_create_user_data(user_type="individual")

        response1 = client.post("/api/v1/users/", json=user_data)
        assert response1.status_code == 201
        duplicate_user_data = make_create_user_data(user_type="individual", **{key_value: user_data[key_value]})
        response2 = client.post("/api/v1/users/", json=duplicate_user_data)
        assert response2.status_code == 400
        assert response2.json()["detail"] == msg
    
    def test_valid_user_can_be_fetched_via_api(self, client):

        user_data = make_create_user_data(user_type="individual")

        response1 = client.post("/api/v1/users/", json=user_data)
        assert response1.status_code == 201
        created_user_id = response1.json()["id"]

        response2 = client.get(f"/api/v1/users/{created_user_id}")
        assert response2.status_code == 200
        fetched_user_data = response2.json()
        assert fetched_user_data["id"] == created_user_id
        assert fetched_user_data["user_name"] == user_data["user_name"]
        assert fetched_user_data["user_type"] == user_data["user_type"]
        assert fetched_user_data["display_name"] == user_data["display_name"]
        assert fetched_user_data["description"] == user_data["description"]
        assert fetched_user_data["email"] == user_data["email"]
        assert fetched_user_data["mobile"] == user_data["mobile"]
    
    def test_nonexistent_user_returns_404_via_api(self, client):

        non_existent_user_id = 9999

        response = client.get(f"/api/v1/users/{non_existent_user_id}")

        assert response.status_code == 404
        assert response.json()["detail"] == f"User with ID {non_existent_user_id} not found"