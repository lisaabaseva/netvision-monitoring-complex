from pydantic import BaseModel
from uuid import UUID


class CameraCreate(BaseModel):
    description: str
    url: str
    id: int
    active: bool
    complex_uuid: UUID