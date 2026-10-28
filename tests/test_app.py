import pytest
from app import app, calculate


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_addition():
    assert calculate(10, 5, "add") == 15


def test_subtraction():
    assert calculate(10, 5, "subtract") == 5


def test_menu_shows_only_push1_operations(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Addition" in response.data
    assert b"Subtraction" in response.data
    assert b"Multiplication" not in response.data
    assert b"Division" not in response.data


def test_health(client):
    assert client.get("/health").json == {"status": "healthy"}