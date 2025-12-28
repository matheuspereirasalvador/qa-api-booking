import requests

url_base = "https://restful-booker.herokuapp.com/booking"
headers = {"Content-Type": "application/json"}


def test_criar_e_consultar_reserva():
    payload = {
        "firstname": "Matheus",
        "lastname": "QA",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-02-01",
            "checkout": "2024-02-05"
        },
        "additionalneeds": "Jantar VIP"
    }

    resposta_post = requests.post(url_base, json=payload, headers=headers)
    assert resposta_post.status_code == 200

    id_criado = resposta_post.json()["bookingid"]
    print(f"\nReserva criada com sucesso! ID Gerado: {id_criado}")

    resposta_get = requests.get(f"{url_base}/{id_criado}")

    print(f"Consultando ID: {id_criado}")
    print(f"Dados retornados: {resposta_get.json()}")

    assert resposta_get.status_code == 200
    dados = resposta_get.json()

    assert dados["firstname"] == "Matheus"
    assert dados["additionalneeds"] == "Jantar VIP"