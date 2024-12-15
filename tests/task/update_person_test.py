import unittest
from fastapi import HTTPException
from src.controllers import TaskController
from src.models import TaskBody
from src.database import Base, engine
from datetime import date

Base.metadata.create_all(bind=engine)

class TestUpdateTask(unittest.TestCase):

    def test_update_task_with_valid_data(self):
        person_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        result = TaskController().create(person_data)

        person_data = TaskBody(
            title="New Task 1", description="test 1", 
            status="done", priority="low", deadline=str(date.today()),
            id_person=0
        )

        id = result['id']
        result = TaskController().update(id, person_data)

        self.assertEqual(result['message'], "Tarefa atualizada com sucesso")

        result2 = TaskController().get(id)

        self.assertEqual(result2['title'], "New Task 1")
        self.assertEqual(result2['description'], "test 1")
        self.assertEqual(result2['status'], "done")
        self.assertEqual(result2['priority'], "low")
        self.assertEqual(result2['deadline'], str(date.today()))
        self.assertEqual(result2['updated_at'], str(date.today()))

    def test_update_task_with_invalid_id(self):
        person_data = TaskBody(
            title="New Task", description="test",
            status="pending", priority="high", deadline=str(date.today()),
            id_person=0
        )

        try:
            result = TaskController().update(-10, person_data)
        
        except HTTPException as e:
            self.assertEqual(e.__str__(), "404: Tarefa não encontrada.")
        
        except Exception:
            self.fail("HTTPException not raised")
