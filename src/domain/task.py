# domain/task.py
class Task:
    def __init__(self, name: str, description: str):
        if not name:
            raise ValueError("Nome da tarefa é obrigatório")
        self.name = name
        self.description = description or ""
        self.status = "pending"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "status": self.status
        }
