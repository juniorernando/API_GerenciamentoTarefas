import pytest
from unittest.mock import MagicMock
from interface.user_controller import create_user_controller
from usecase.addtask import CreateUserUseCase

@pytest.fixture
def mock_usecase(mocker):
    return mocker.patch('interface.user_controller.CreateUserUseCase', autospec=True)

def test_controller_success(mock_usecase):
    # Configurar o mock do usecase
    usecase_instance = mock_usecase.return_value
    usecase_instance.execute.return_value = {"status": "success", "task": {"id": 1, "name": "Teste", "description": "Descrição de teste", "status": "pending"}}
    
    # Testar controller com dados válidos
    body = {
        "name": "Teste",
        "description": "Descrição de teste",
        "db_username": "admin",
        "db_password": "senha123"
    }
    
    response = create_user_controller(body)
    assert response["statusCode"] == 200
    assert response["body"]["status"] == "success"

def test_controller_missing_fields():
    # Testar controller com campos faltando
    body = {
        "name": "Teste"
        # description está faltando
    }

    response = create_user_controller(body)
    assert response["statusCode"] == 400
    assert "error" in response["body"]
    assert response["body"]["error"] == "Nome e descrição são campos obrigatórios"

def test_controller_authentication_error(mock_usecase):
    # Configurar o mock do usecase para lançar erro de autenticação
    usecase_instance = mock_usecase.return_value
    usecase_instance.execute.side_effect = PermissionError("Credenciais inválidas")

    # Testar controller com credenciais inválidas
    body = {
        "name": "Teste",
        "description": "Descrição de teste",
        "db_username": "wrong",
        "db_password": "wrong"
    }

    response = create_user_controller(body)
    assert response["statusCode"] == 401
    assert "error" in response["body"]
    assert response["body"]["error"] == "Credenciais inválidas"