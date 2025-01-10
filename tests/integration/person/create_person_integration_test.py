import unittest
import requests


class TestCreatePersonIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.token = requests\
            .post("http://localhost:8000/token", data={"username": "user", "password": "password"})\
            .json()\
            .get("access_token")

        return super().setUpClass()

    def test_integration_create_person_with_valid_data(self):
        person_data = {
            "name": "New Person",
            "email": "teste@teste.com",
            "phone": "12345678901"
        }

        result = requests\
            .post("http://localhost:8000/person/create", json=person_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json().get("name"), "New Person")
        self.assertEqual(result.json().get("email"), "teste@teste.com")
        self.assertEqual(result.json().get("phone"), "12345678901")
        self.assertIn('id', result.json())

    def test_integration_create_task_with_phone_error(self):
        person_data = {
            "name": "New Person",
            "email": "teste@teste.com",
            "phone": "fd"
        }

        result = requests\
            .post("http://localhost:8000/person/create", json=person_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 422)
        self.assertIn("Telefone inválido",
                      result.json().get("detail")[0].get("msg"))

    def test_integration_create_task_with_email_error(self):
        person_data = {
            "name": "New Person",
            "email": "teste.com",
            "phone": "12345678901"
        }

        result = requests\
            .post("http://localhost:8000/person/create", json=person_data, headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(result.status_code, 422)
        self.assertIn("Email inválido", result.json().get(
            "detail")[0].get("msg"))
