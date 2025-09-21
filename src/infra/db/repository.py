# infra/db/repository.py
from infra.db.db import Database
from infra.logging.logger import ContextLogger, with_correlation

logger = ContextLogger()

class TaskRepository:
    # Repositório de tarefas
    def __init__(self, db_username: str = None, db_password: str = None):
        logger.info("Iniciando Repository")
        self.db = Database(username=db_username, password=db_password)

    @with_correlation
    # Salva a tarefa no banco de dados
    def save(self, task):
        logger.info("Repository iniciando operação de save")
        result = self.db.insert(task.to_dict())
        logger.info(f"Repository finalizou operação de save: {result}")
        return result
