from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_save_joke():
    test_joke = 'This is a very simple test joke. It is not funny :('
    response = client.post('/jokes/?joke={}'.format(test_joke))
    assert response.status_code == 201
    assert response.json()["joke"] == test_joke
    assert response.json()["joke_from"] == 'User'


def test_get_random_joke():
    response = client.get('/jokes/')
    assert response.status_code == 200
    assert response.json()["id"] is None
    assert response.json()["joke_from"] == 'Chuck' or 'Dad'


def test_get_random_chuck_joke():
    response = client.get('/jokes/Chuck/')
    assert response.status_code == 200
    assert response.json()["id"] is None
    assert response.json()["joke_from"] == 'Chuck'


def test_get_random_dad_joke():
    response = client.get('/jokes/Dad/')
    assert response.status_code == 200
    assert response.json()["id"] is None
    assert response.json()["joke_from"] == 'Dad'


def test_get_random_joke_422_error():
    response = client.get('/jokes/gg/')
    assert response.status_code == 422


def test_update_joke():
    updated_joke = 'This a updated joke UwU'
    response = client.patch('/jokes/1/?joke={}'.format(updated_joke))
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "joke": updated_joke,
        "joke_from": "User"
    }


def test_delete_joke():
    deleted_joke = 8
    response = client.delete('/jokes/{}/'.format(deleted_joke))
    assert response.status_code == 200
    assert response.json() == {
        "operation": "Deleted joke with id: {}".format(deleted_joke),
        "successful": True
    }


def test_not_found_joke():
    id_joke = 8
    response = client.patch('/jokes/{}/'.format(id_joke))
    assert response.status_code == 404
