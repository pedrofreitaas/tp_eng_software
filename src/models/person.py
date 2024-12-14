from pydantic import BaseModel

class PersonBody(BaseModel):
    name: str
    email: str