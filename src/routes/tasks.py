from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import HTTPBasicCredentials

# from src.controllers import TasksController
from src.models import TaskParams
from src.services import get_current_credentials

router = APIRouter(tags=["Tasks"])

#tasks_controller = TasksController()

@router.get("/get_task", status_code=201, tags=["get", "NEW"])
def run_bot(
    request: Request,
    task_params: TaskParams,
    _: Annotated[HTTPBasicCredentials, Depends(get_current_credentials)],
):
    """
    

    Args:
        BLABLA
        _: Dependency to validate current user credentials.

    Returns:
        Response description.
    """
    try:
        return None
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred.",
        )
