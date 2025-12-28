import requests

url_base = "https://restful-booker.herokuapp.com/booking"
headers_padrao = {"Content-Type": "application/json"}

def test_atualizar_reserva(token):
    payload_original = {
        "firstname": "Matheus",
        "lastname": "QA",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-02"},
        "additionalneeds": "Agua"
    }
    resposta_create = requests.post(url_base, json=payload_original, headers=headers_padrao)
    booking_id = resposta_create.json()["bookingid"]

    headers_auth = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    payload_atualizado = {
        "firstname": "Matheus VIP",
        "lastname": "QA Sênior",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-02"},
        "additionalneeds": "Champagne"
    }

    url_put = f"{url_base}/{booking_id}"
    resposta_put = requests.put(url_put, json=payload_atualizado, headers=headers_auth)

    assert resposta_put.status_code == 200
    dados = resposta_put.json()

    print(f"\nReserva {booking_id} atualizada!")
    print(f"Novo nome: {dados['firstname']}")

    assert dados["firstname"] == "Matheus VIP"
    assert dados["additionalneeds"] == "Champagne"