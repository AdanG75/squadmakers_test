from fastapi.testclient import TestClient

from main import app


ID_JOKE_TO_TEST = 13


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
    updated_joke_id = ID_JOKE_TO_TEST
    response = client.patch('/jokes/{}/?joke={}'.format(updated_joke_id, updated_joke))
    assert response.status_code == 200
    assert response.json() == {
        "id": updated_joke_id,
        "joke": updated_joke,
        "joke_from": "User"
    }


def test_delete_joke():
    deleted_joke = ID_JOKE_TO_TEST
    response = client.delete('/jokes/{}/'.format(deleted_joke))
    assert response.status_code == 200
    assert response.json() == {
        "operation": "Deleted joke with id: {}".format(deleted_joke),
        "successful": True
    }


def test_not_found_joke():
    id_joke = ID_JOKE_TO_TEST
    response = client.patch('/jokes/{}/'.format(id_joke))
    assert response.status_code == 404
