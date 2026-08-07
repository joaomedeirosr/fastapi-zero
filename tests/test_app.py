from fastapi.testclient import TestClient
from http import HTTPStatus
from src.app import app


def test_root_return_hello():
    """
    Esse teste e um teste de 3 etapas ou tambem conhecido como triple A - (AAA)

    - A: Arrange - Arranjo e o que preciso ter antes do teste comecar
    - A: Act - Eu preciso atuar/agir e o responsavel por executar o que preciso (O SUT) - System under test
    - A: Assert - Garante que aquilo que estou testando e uma verdade ou algo seja resolvido/respondido
    """

    # Arrange cria o objeto e envolpa um outro objeto app (wrapper) - Organiza
    client = TestClient(app)

    # Act - chama get
    response = client.get('/')
    #Assert
    assert response.json() == {'msg': 'Hello world'}
    assert response.status_code == HTTPStatus.OK