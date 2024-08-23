from pydantic import BaseModel
from uuid import UUID


class CameraStatesUpdate(BaseModel):
    uuid: UUID
    status: int
    active: bool