from pydantic import BaseModel
from uuid import UUID


class GroupOut(BaseModel):
    uuid: UUID
    name: str
