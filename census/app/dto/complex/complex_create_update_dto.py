from pydantic import BaseModel
from uuid import UUID


class ComplexOut(BaseModel):
    uuid: UUID
    name: str
    ip: str
    port: int
    login: str
    password: str
    group_uuid: UUID
