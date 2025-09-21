import pytest
from unittest.mock import MagicMock
from infra.db.authenticator import DatabaseAuthenticator
from infra.logging.logger import ContextLogger

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('infra.db.authenticator.ContextLogger', autospec=True)

def test_authenticator_valid_credentials():
    # Teste com credenciais válidas
    authenticator = DatabaseAuthenticator(username="admin", password="senha123")
    assert authenticator.authenticate() == True
    assert authenticator.is_authenticated == True

def test_authenticator_invalid_credentials():
    # Teste com credenciais inválidas
    authenticator = DatabaseAuthenticator(username="wrong", password="wrong")
    assert authenticator.authenticate() == False
    assert authenticator.is_authenticated == False

def test_authenticator_missing_credentials():
    # Teste com credenciais faltando
    authenticator = DatabaseAuthenticator()
    assert authenticator.authenticate() == False
    assert authenticator.is_authenticated == False

def test_validate_connection_authenticated():
    # Teste validação com autenticação
    authenticator = DatabaseAuthenticator(username="admin", password="senha123")
    authenticator.authenticate()
    # Não deve levantar exceção
    authenticator.validate_connection()

def test_validate_connection_not_authenticated():
    # Teste validação sem autenticação
    authenticator = DatabaseAuthenticator(username="wrong", password="wrong")
    authenticator.authenticate()
    with pytest.raises(PermissionError):
        authenticator.validate_connection()
