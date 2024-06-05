from .conftest import client


def test_should_status_code_ok(client):
    response = client.get('/')
    data = response.data.decode()
    assert data == "Hello World!!"
    