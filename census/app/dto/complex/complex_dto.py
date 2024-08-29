from pydantic import BaseModel
from uuid import UUID


class ComplexCreate(BaseModel):
    """Класс ComplexCreate - это DTO для создания нового комплекса в группе."""
    name: str
    ip: str
    port: int
    login: str
    password: str
    group_uuid: UUID
