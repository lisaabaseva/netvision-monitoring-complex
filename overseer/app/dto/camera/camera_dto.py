from pydantic import BaseModel
from uuid import UUID


# Здесь был CameraIn. Используется в overseer/app/service/complex.py
class CameraDto(BaseModel):
    id: int
    description: str
    url: str
    active: bool
    status: int

