from pydantic import BaseModel
from uuid import UUID


class CameraIn(BaseModel):
    uuid: UUID
    ip: str
    port: int
    status: int
    group_uuid: UUID