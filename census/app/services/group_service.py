import uuid

from repository import GroupRepository
from dto.group import GroupCreate
from model import Group


class GroupService:
    def __init__(self, group_repository: GroupRepository):
        self.group_repository = group_repository

    def get_groups(self) -> list[Group]:
        return self.group_repository.get_groups()

    def create_group(self, group_create: GroupCreate) -> Group:
        new_group: Group = Group(name=group_create.name)
        return self.group_repository.create_group(new_group)

    def delete_group_by_id(self, group_id: uuid.UUID) -> bool:
        return self.group_repository.delete_group_by_id(group_id)
