from src.services import TaskService

class TaskController:
    def __init__(self):
        self.task_service = TaskService()

    def create(self, task_data: dict) -> dict:
        return self.task_service.create(task_data)