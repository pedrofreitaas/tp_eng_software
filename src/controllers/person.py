from src.services import PersonService
from src.models import PersonBody
class PersonController:
    def __init__(self):
        self.person_service = PersonService()

    def create(self, person_data: PersonBody) -> dict:
        return self.person_service.create(person_data)
