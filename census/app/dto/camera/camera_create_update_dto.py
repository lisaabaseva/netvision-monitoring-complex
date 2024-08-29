from pydantic import BaseModel
from uuid import UUID


class CameraOut(BaseModel):
    """Класс CameraOut - это DTO для полученных данных от overseer."""
    uuid: UUID
    description: str
    id: int
    url: str
    status: int
    active: bool
    complex_uuid: UUID
