from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_add_one():
    response = client.get("/numbers/add-one/4/")
    assert response.status_code == 200
    assert response.json() == {
        "operation": "Add one",
        "result": 5
    }


def test_add_one_422_error():
    response = client.get("/numbers/add-one/hi/")
    assert response.status_code == 422


def test_lcm():
    response = client.get("/numbers/mcm/?numbers=45&numbers=60&numbers=12&numbers=13&numbers=93&numbers=61")
    assert response.status_code == 200
    assert response.json() == {
        "operation": "Least Common Multiple",
        "result": 4424940
    }


def test_lcm_none():
    response = client.get("/numbers/mcm/?")
    assert response.status_code == 200
    assert response.json() == {
        "operation": "Least Common Multiple",
        "result": 0
    }


def test_lcm_zero():
    response = client.get("/numbers/mcm/?numbers=45&numbers=60&numbers=12&numbers=0&numbers=93&numbers=61")
    assert response.status_code == 200
    assert response.json() == {
        "operation": "Least Common Multiple",
        "result": 0
    }


def test_lcm_one_number():
    response = client.get("/numbers/mcm/?numbers=8")
    assert response.status_code == 200
    assert response.json() == {
        "operation": "Least Common Multiple",
        "result": 8
    }


def test_lcm_422_error():
    response = client.get("/numbers/mcm/?numbers=25&numbers=2&numbers=95&numbers=hola&numbers=6")
    assert response.status_code == 422
