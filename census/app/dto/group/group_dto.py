from pydantic import BaseModel


class GroupCreate(BaseModel):
    """Класс GroupCreate - это DTO для создания новой группы."""
    name: str
