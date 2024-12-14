from src.database import SessionLocal
from src.models import TaskBody
from src.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import date


class TaskRepository(Base):
    __tablename__ = "task"
    db = SessionLocal()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    deadline = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    id_person = Column(Integer, ForeignKey("person.id"), nullable=True)

    def create(self, task_data: TaskBody)-> int:
        task = TaskRepository(**task_data.__dict__)
        task.created_at = date.today()

        self.db.add(task)
        self.db.commit()

        return self.db.query(TaskRepository).order_by(TaskRepository.id.desc()).first().__dict__
