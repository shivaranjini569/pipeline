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


def test_multiplication():
    assert calculate(10, 5, "multiply") == 50


def test_division():
    assert calculate(10, 5, "divide") == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, 0, "divide")


def test_menu_shows_all_four_operations(client):
    response = client.get("/")
    assert response.status_code == 200
    for label in (b"Addition", b"Subtraction", b"Multiplication", b"Division"):
        assert label in response.data


def test_health(client):
    assert client.get("/health").json == {"status": "healthy"}