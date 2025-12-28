import requests


def test_api_esta_online():
    url = "https://restful-booker.herokuapp.com/ping"
    resposta = requests.get(url)

    assert resposta.status_code == 201

    print("\nAPI está viva! O servidor respondeu.")