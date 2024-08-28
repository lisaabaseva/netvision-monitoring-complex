import uuid

from sqlmodel import select
from sqlmodel import Session

from model import Group
from dto.group import GroupCreate
from config.init_db import get_session


class GroupRepository:
    def get_groups(self) -> list[Group]:
        session: Session = next(get_session())
        result = session.scalars(select(Group)).all()
        session.close()
        return [Group(uuid=group.uuid, name=group.name) for group in result]

    def create_group(self, group_create: GroupCreate) -> Group:
        session: Session = next(get_session())

        session.add(group_create)
        session.commit()
        session.refresh(group_create)
        session.close()
        return group_create

    def delete_group_by_id(self, group_id: uuid.UUID) -> bool:
        session: Session = next(get_session())
        result = session.get(Group, group_id)

        if result is None:
            return False

        session.delete(result)
        session.commit()
        session.close()
        return True