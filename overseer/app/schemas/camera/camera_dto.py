from pydantic import BaseModel
from uuid import UUID


class CameraDto(BaseModel):
    id: int
    description: str
    url: str
    active: bool
    status: int


class CameraStatusDto(BaseModel):
    id: int
    status: int
    active: bool
