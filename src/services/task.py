from src.repositories import TaskRepository
from src.models import TaskBody

class TaskService:
    def __init__(self) -> None:
        self.__repository = TaskRepository()

    def create(self, task_data: TaskBody) -> dict:
        return self.__repository.create(task_data)