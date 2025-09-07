import pytest
from unittest.mock import MagicMock
from infra.db.db import Database
from infra.db.authenticator import DatabaseAuthenticator

@pytest.fixture
def mock_authenticator(mocker):
    authenticator = mocker.Mock(spec=DatabaseAuthenticator)
    authenticator.is_authenticated = True
    return authenticator

def test_database_insert_authenticated(mock_authenticator):
    # Teste inserção com autenticação
    db = Database(username="admin", password="senha123")
    db._authenticator = mock_authenticator
    
    result = db.insert({"name": "Teste", "description": "Descrição"})
    assert result["id"] == 1
    assert result["name"] == "Teste"
    assert result["description"] == "Descrição"

def test_database_insert_not_authenticated():
    # Teste inserção sem autenticação
    with pytest.raises(PermissionError) as exc_info:
        db = Database(username="wrong", password="wrong")
    assert str(exc_info.value) == "Não foi possível conectar ao banco de dados. Verifique suas credenciais."
