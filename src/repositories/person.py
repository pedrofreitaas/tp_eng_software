from src.database import SessionLocal
from src.models import PersonBody
from src.database.database import Base
from sqlalchemy import Column, Integer, String
from datetime import date
class PersonRepository(Base):
    __tablename__ = "person"
    db = SessionLocal()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)   
    phone = Column(String, nullable=False)
    created_at = Column(String, nullable=False)


    def create(self, person_data: PersonBody)-> None:
        person = PersonRepository(**person_data.__dict__)
        person.created_at = date.today()

        self.db.add(person)
        self.db.commit()
        
        return self.db.query(PersonRepository).order_by(PersonRepository.id.desc()).first().__dict__

    def get(self, id: int)-> dict:
        result = self.db.query(PersonRepository).filter(PersonRepository.id == id).first()
        if result:
            return result.__dict__
        return None
    
    def delete(self, id: int)-> None:
        person = self.db.query(PersonRepository).filter(PersonRepository.id == id).first()
        self.db.delete(person)
        self.db.commit()
        return {"message": "Pessoa deletada com sucesso"}
        