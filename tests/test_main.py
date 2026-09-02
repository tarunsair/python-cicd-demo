from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from Python CI/CD!"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_hello():
    response = client.get("/hello/Tarun")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, Tarun!"
    }