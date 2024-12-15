from src.services import TaskService
from src.models import TaskBody
class TaskController:
    def __init__(self):
        self.task_service = TaskService()

    def create(self, task_data: TaskBody) -> dict:
        return self.task_service.create(task_data)
    
    def get(self, id: int) -> dict:
        return self.task_service.get(id)

    def update(self, id: int, task_data: TaskBody) -> dict:
        return self.task_service.update(id, task_data)
    
    def delete(self, id: int) -> dict:
        return self.task_service.delete(id)
