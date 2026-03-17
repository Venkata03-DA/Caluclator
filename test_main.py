from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test 1: Home route returns correct message
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


# Test 2: Add two numbers
def test_add():
    response = client.get("/add?a=3&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


# Test 3: Subtract two numbers
def test_subtract():
    response = client.get("/subtract?a=10&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}


# Test 4: Multiply two numbers
def test_multiply():
    response = client.get("/multiply?a=4&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 12}


# Test 5: Add with negative numbers
def test_add_negative():
    response = client.get("/add?a=-5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": -2}
