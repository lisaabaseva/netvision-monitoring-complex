from pydantic import BaseModel
from uuid import UUID


class ComplexOut(BaseModel):
    """Класс ComplexOut - это DTO для полученных данных из БД для отправки UI."""
    uuid: UUID
    name: str
    ip: str
    port: int
    login: str
    password: str
    group_uuid: UUID
