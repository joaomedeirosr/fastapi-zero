from http import HTTPStatus

from fastapi.testclient import TestClient

from src.lecture import app


def test_lecture():
    test_client = TestClient(app)

    response = test_client.get('/lectures')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Ola mundo</h1>' in response.text
