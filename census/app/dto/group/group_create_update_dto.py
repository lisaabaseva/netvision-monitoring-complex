from pydantic import BaseModel
from uuid import UUID


class GroupOut(BaseModel):
    """Класс GroupOut - это DTO для получения информации о группе."""
    uuid: UUID
    name: str
