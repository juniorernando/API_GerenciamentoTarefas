import pytest
from unittest.mock import patch, MagicMock
from lambda_handler import lambda_handler
from infra.db.repository import TaskRepository
from infra.db.authenticator import DatabaseAuthenticator

@pytest.fixture
def mock_repository():
    repository = MagicMock(spec=TaskRepository)
    repository.save.return_value = {"status": "success", "task_id": 1}
    return repository

@pytest.fixture
def mock_authenticator():
    authenticator = MagicMock(spec=DatabaseAuthenticator)
    authenticator.authenticate.return_value = True
    return authenticator

@patch('usecase.addtask.TaskRepository')
@patch('usecase.addtask.DatabaseAuthenticator')
def test_with_valid_credentials(mock_auth_class, mock_repo_class, mock_repository, mock_authenticator):
    mock_repo_class.return_value = mock_repository
    mock_auth_class.return_value = mock_authenticator
    
    event = {
        "body": {
            "name": "Estudar Python",
            "description": "Aprender mais sobre Python e seus frameworks",
            "db_username": "admin",
            "db_password": "senha123"
        }
    }
    
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
    assert "correlation_id" in response["body"]
    # O autenticador é inicializado com as credenciais e depois authenticate() é chamado
    mock_auth_class.assert_called_once_with(username="admin", password="senha123")
    mock_authenticator.authenticate.assert_called_once_with()
    mock_repository.save.assert_called_once()

@patch('usecase.addtask.TaskRepository')
@patch('usecase.addtask.DatabaseAuthenticator')
def test_with_invalid_credentials(mock_auth_class, mock_repo_class, mock_repository, mock_authenticator):
    mock_repo_class.return_value = mock_repository
    mock_authenticator = mock_auth_class.return_value
    mock_authenticator.authenticate.return_value = False
    
    event = {
        "body": {
            "name": "Estudar Python",
            "description": "Aprender mais sobre Python e seus frameworks",
            "db_username": "usuario_errado",
            "db_password": "senha_errada"
        }
    }
    
    response = lambda_handler(event, None)
    assert response["statusCode"] == 401
    assert "error" in response["body"]
    # O autenticador é inicializado com as credenciais e depois authenticate() é chamado
    mock_auth_class.assert_called_once_with(username="usuario_errado", password="senha_errada")
    mock_authenticator.authenticate.assert_called_once_with()
    mock_repository.save.assert_not_called()
