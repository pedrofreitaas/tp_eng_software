from pydantic import BaseModel


class TaskParams(BaseModel):
    """
    Represents a generic task with various attributes.

    Each field corresponds to a specific attribute of the task that can be optionally specified.
    Fields default to empty values when not provided.
    """

    # put the fields here.
    description: str | None = ""
