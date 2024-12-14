from pydantic import BaseModel

class TaskBody(BaseModel):
    title: str
    description: str
    deadline: str
    priority: str
    status: str
    id_person: int | None = None