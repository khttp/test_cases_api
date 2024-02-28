import pytest
from models.model import db,TestAsset,TestCase,TestResult
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
    data = {"id":1,"name":"test_case_1",
            "description":"test_case_1 description"}
    response = client.post('/create_test_case',json=data)
    print(response.json)
    assert response.status_code == 201

@pytest.fixture
def create_test_asset(client):
    """Test the index route."""
    data={"id":1,"name":"test_asset_1",
        "test_case_id":1}
    response = client.post('/create_test_asset',json=data)
    assert response.status_code == 201
    return data["id"]

@pytest.fixture
def create_results(client):
    """Test retrieving the testcases."""
    data={"result":"test_result_1",
        "test_case_id":1,"test_asset_id":1}
    response= client.post("/get_test_cases",json=data)

def test_create_test_case(client):
    """Test the index route."""
    data = {"id":1,"name":"test_case_1",
            "description":"test_case_1 description"}
    response = client.post('/create_test_case',json=data)
    assert response.status_code == 201
     
def test_get_test_assets(client):
    """Test retrieving the testcases."""
    response= client.get("/get_test_assets")
    assert response.status_code == 200


def test_create_test_results(client,create_test_case,create_test_asset):    
    """Test the index route."""
    create_test_asset
    create_test_case
    data={"result":"test_result_1",
        "test_case_id":1,"test_asset_id":1}
    response= client.post("/create_test_result",json=data)
    assert response.status_code == 201

def test_get_test_results(client,create_results,create_test_case,create_test_asset):
    id =create_test_asset
    """Test retrieving the testcases."""
    response= client.get(f"/get_test_results/{id}")
    assert response.status_code == 200
# Write additional test functions for other endpoints
