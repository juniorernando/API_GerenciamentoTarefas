# infra/db/db.py
from infra.db.authenticator import DatabaseAuthenticator
from infra.logging.logger import ContextLogger, with_correlation

logger = ContextLogger()

class Database:
    def __init__(self, username: str = None, password: str = None):
        self.tasks = []
        logger.info("Inicializando conexão com o banco de dados")
        self._authenticator = DatabaseAuthenticator(username, password)
        self._connect()
        
    def _connect(self):
        """Conecta e autentica no banco de dados"""
        logger.info("Tentando autenticar no banco de dados")
        if self._authenticator.authenticate():
            logger.info("Conexão com o banco de dados estabelecida com sucesso!")
        else:
            logger.error("Falha na autenticação do banco de dados")
            raise PermissionError("Não foi possível conectar ao banco de dados. Verifique suas credenciais.")
        
    @with_correlation
    def insert(self, task_data: dict):
        self._authenticator.validate_connection()
        logger.info(f"Salvando task no banco: {task_data}")
        task_id = len(self.tasks) + 1
        task_data["id"] = task_id
        self.tasks.append(task_data)
        logger.info(f"Task salva com sucesso. ID: {task_id}")
        return task_data
