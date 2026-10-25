
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool = False


class TaskCreate(TaskBase):
    id: int


class TaskResponse(TaskBase):
    id: int

    model_config = {"from_attributes": True}
