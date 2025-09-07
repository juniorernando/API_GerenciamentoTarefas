from lambda_handler import lambda_handler

def test_with_valid_credentials():
    print("\n🧪 Testando com credenciais válidas:")
    event = {
        "body": {
            "name": "Estudar Python",
            "description": "Aprender mais sobre Python e seus frameworks",
            "db_username": "admin",
            "db_password": "senha123"
        }
    }
    response = lambda_handler(event, None)
    print("Resposta:", response)

def test_with_invalid_credentials():
    print("\n🧪 Testando com credenciais inválidas:")
    event = {
        "body": {
            "name": "Estudar Python",
            "description": "Aprender mais sobre Python e seus frameworks",
            "db_username": "usuario_errado",
            "db_password": "senha_errada"
        }
    }
    response = lambda_handler(event, None)
    print("Resposta:", response)

if __name__ == "__main__":
    test_with_valid_credentials()
    test_with_invalid_credentials()
