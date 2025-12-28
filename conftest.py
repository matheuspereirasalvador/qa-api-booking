import pytest
import requests


@pytest.fixture
def token():
    url = "https://restful-booker.herokuapp.com/auth"
    payload = {
        "username": "admin",
        "password": "password123"
    }

    resposta = requests.post(url, json=payload)
    assert resposta.status_code == 200

    return resposta.json()["token"]