from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPBasicCredentials

from src.controllers import TaskController
from src.models import TaskBody
from src.services import get_current_credentials

router = APIRouter(tags=["Tasks"])

task_controller = TaskController()

@router.post("/tasks/create", status_code=200)
def create_task(
    body: TaskBody,
    credentials: HTTPBasicCredentials = Depends(get_current_credentials),
):
    try:
        return task_controller.create(body)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        )