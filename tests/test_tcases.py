import pytest
from models.model import db ,TestCase
from app import create_app
from flask import json

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            # Set up test database
            db.create_all()
        yield client
        with app.app_context():
            # Clean up test database
            db.session.remove()
            db.drop_all() 
@pytest.fixture
def create_test_case(client):
    """Test the index route."""
    data={"id":1,"name":"test_case_1",
          "description":"test_case_1 description"}
    response = client.post('/create_test_case',json=data)
    assert response.status_code == 201
    return data["id"]

def test_create_test_case(client):
    """Test the index route."""
    data={"name":"test_case_1",
          "description":"test_case_1 description"}
    response = client.post('/create_test_case',json=data)
    assert response.status_code == 201

def test_get_test_cases(client):
    """Test retrieving the testcases."""
    response= client.get("/get_test_cases")
    assert response.status_code == 200

def test_get_test_case(client,create_test_case):
    """Test retrieving the testcases."""
    caseid = create_test_case
    response= client.get(f'/get_test_case/{caseid}')
    assert response.status_code == 200

def test_update_test_case(client,create_test_case):
    """Test updating the testcases."""
    caseid = create_test_case
    data={"id":caseid,"name":"test_case_1",
          "description":"test_case_1 description"}
    response= client.put(f'/update_test_case/{caseid}',json=data)
    assert response.status_code == 200     

def test_delete_test_case(client,create_test_case):
    """Test deleting the testcases."""
    caseid = create_test_case
    response= client.delete(f'/delete_test_case/{caseid}')
    assert response.status_code == 200