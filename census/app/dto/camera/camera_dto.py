from pydantic import BaseModel
from uuid import UUID


class CameraCreate(BaseModel):
    """Класс CameraCreate - это DTO для создания новой камеры в комплексе."""
    description: str
    url: str
    id: int
    status: int
    active: bool
    complex_uuid: UUID
