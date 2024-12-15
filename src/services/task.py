from src.repositories import TaskRepository
from src.models import TaskBody
from fastapi import HTTPException

class TaskService:
    def __init__(self) -> None:
        self.__repository = TaskRepository()

    def create(self, task_data: TaskBody) -> dict:
        return self.__repository.create(task_data)
    
    def delete(self, id: int) -> dict:
        task = self.__repository.get(id)
        if not task:
            raise HTTPException(status_code=404, detail="Tarefa não Encontrada.")
        return self.__repository.delete(id)