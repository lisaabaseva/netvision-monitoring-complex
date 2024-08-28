from pydantic import BaseModel
from uuid import UUID


class CameraOut(BaseModel):
    uuid: UUID
    description: str
    id: int
    url: str
    status: int
    active: bool
    complex_uuid: UUID
