import uuid

from repository import GroupRepository
from dto.group import GroupCreate
from model import Group


class GroupService:
    """Класс GroupService предоставляет набор методов для взаимодействия с моделью группы и репозиторием."""
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def get_groups(self) -> list[Group]:
        """Возвращает список всех групп в БД."""
        return self.group_repository.get_groups()

    def create_group(self, group_create: GroupCreate) -> Group:
        """Создает новую группу в БД."""
        new_group: Group = Group(name=group_create.name)
        return self.group_repository.create_group(new_group)

    def delete_group_by_id(self, group_id: uuid.UUID) -> bool:
        """Удаляет из БД группу по ее ID."""
        return self.group_repository.delete_group_by_id(group_id)
