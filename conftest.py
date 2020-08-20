from pytest import fixture


@fixture
def sent(mocker):
    return mocker.sentinel


@fixture
def client_app():
    from infrastructure.web.fastapi.main import app
    from fastapi.testclient import TestClient
    return TestClient(app)
