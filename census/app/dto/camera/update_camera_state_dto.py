from pydantic import BaseModel
from uuid import UUID


class StatusesUpdate(BaseModel):
    uuid: UUID
    status: int
    active: bool