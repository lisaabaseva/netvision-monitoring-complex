from pydantic import BaseModel
from uuid import UUID


class ComplexCreate(BaseModel):
    name: str
    ip: str
    port: int
    login: str
    password: str
    group_uuid: UUID
