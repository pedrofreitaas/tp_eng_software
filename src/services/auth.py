import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.config import envs

security = HTTPBasic()


def get_current_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> HTTPBasicCredentials:
    """
    Validates the username and password using Basic Authentication.

    This function compares the provided credentials (username and password) with the
    values stored in the environment configuration. If the credentials are correct,
    it returns the provided credentials; otherwise, it raises an HTTP 401 Unauthorized error.

    Args:
        credentials (HTTPBasicCredentials): The credentials provided by the user in the Basic Auth header.

    Returns:
        HTTPBasicCredentials: The credentials provided by the user if authentication is successful.

    Raises:
        HTTPException: If the provided credentials are incorrect, a 401 Unauthorized exception is raised.
    """
    try:
        current_username_bytes = credentials.username.encode("utf8")
        correct_username_bytes = envs.basic_auth_username.encode("utf8")

        is_correct_username = secrets.compare_digest(
            current_username_bytes, correct_username_bytes
        )

        current_password_bytes = credentials.password.encode("utf8")
        correct_password_bytes = envs.basic_auth_password.encode("utf8")

        is_correct_password = secrets.compare_digest(
            current_password_bytes, correct_password_bytes
        )

        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )

        return credentials
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal error occurred during authentication.",
        )
