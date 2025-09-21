import pytest
from domain.task import Task

def test_task_creation():
    # Teste criação básica de tarefa
    task = Task("Estudar Python", "Aprender mais sobre testes")
    assert task.name == "Estudar Python"
    assert task.description == "Aprender mais sobre testes"
    assert task.status == "pending"

def test_task_to_dict():
    # Teste conversão de tarefa para dicionário
    task = Task("Estudar Python", "Aprender mais sobre testes")
    task_dict = task.to_dict()
    assert task_dict["name"] == "Estudar Python"
    assert task_dict["description"] == "Aprender mais sobre testes"
    assert task_dict["status"] == "pending"
