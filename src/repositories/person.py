from src.database import SessionLocal
from src.models import PersonBody
from src.database.database import Base
from sqlalchemy import Column, Integer, String, Date

class PersonRepository(Base):
    __tablename__ = "person"
    db = SessionLocal()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)   
    phone = Column(String, nullable=False)
    created_at = Column(Date, nullable=False, default="CURRENT_TIMESTAMP")


    def create(self, person: PersonBody)-> None:
        self.db.add(person)