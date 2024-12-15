from src.repositories import PersonRepository
from src.models import PersonBody

class PersonService:
    def __init__(self) -> None:
        self.__repository = PersonRepository()

    def create(self, person_data: PersonBody) -> dict:
        return self.__repository.create(person_data)