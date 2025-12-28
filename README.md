# 🏨 API Automation - Restful Booker

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Requests](https://img.shields.io/badge/Library-Requests-orange.svg)
![Pytest](https://img.shields.io/badge/Framework-Pytest-green.svg)

Projeto de automação de testes de API (Backend) validando o ciclo de vida completo de uma reserva (CRUD) na API [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html).

## 🧠 Destaques Técnicos

* **Automação de API REST:** Uso da biblioteca `requests` para verbos GET, POST, PUT e DELETE.
* **Autenticação:** Gestão de Token via `Pytest Fixtures` (setup automático de login antes dos testes sensíveis).
* **Testes Autossuficientes:** Nenhum teste depende de dados fixos (hardcoded). O script cria, usa e apaga seus próprios dados, permitindo execução paralela e contínua.
* **Health Check:** Validação de disponibilidade do ambiente antes da execução da suíte.
* **Contratos:** Validação de Status Codes e estrutura de JSON.

## 🧪 Cenários Cobertos

1.  ✅ **Health Check:** Verificar se a API está online (Ping).
2.  🆕 **Create Booking:** Criar uma nova reserva e validar o ID gerado.
3.  🔍 **Get Booking:** Consultar os dados da reserva recém-criada.
4.  🔐 **Update Booking:** Gerar token de admin e atualizar dados da reserva (PUT).
5.  🗑️ **Delete Booking:** Apagar a reserva e validar se ela realmente sumiu (404 Not Found).

## 🛠️ Como Rodar Localmente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/matheuspereirasalvador/qa-api-booking.git
    cd qa-api-booking
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute os testes:**
    ```bash
    # Rodar com logs detalhados no terminal
    pytest -v -s
    ```

---
Desenvolvido por **Matheus Pereira Salvador**.