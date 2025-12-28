import requests

url_base = "https://restful-booker.herokuapp.com/booking"
headers_padrao = {"Content-Type": "application/json"}


def test_deletar_reserva(token):
    payload = {
        "firstname": "Reserva",
        "lastname": "Para Deletar",
        "totalprice": 50,
        "depositpaid": False,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-02"},
        "additionalneeds": "Nada"
    }
    resposta_create = requests.post(url_base, json=payload, headers=headers_padrao)
    booking_id = resposta_create.json()["bookingid"]

    print(f"\nReserva criada para extermínio. ID: {booking_id}")

    headers_auth = {"Cookie": f"token={token}"}
    url_delete = f"{url_base}/{booking_id}"

    resposta_delete = requests.delete(url_delete, headers=headers_auth)

    assert resposta_delete.status_code == 201

    print("Comando de deletar enviado com sucesso!")

    resposta_get = requests.get(url_delete)

    print(f"Tentativa de busca pós-delete retornou status: {resposta_get.status_code}")

    assert resposta_get.status_code == 404