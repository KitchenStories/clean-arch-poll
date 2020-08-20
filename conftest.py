from pytest import fixture


@fixture
def sent(mocker):
    return mocker.sentinel


@fixture
def client_app():
    from infrastructure.web.main import app
    from fastapi.testclient import TestClient
    return TestClient(app)
