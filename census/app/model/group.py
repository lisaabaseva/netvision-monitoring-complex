from uuid import uuid4

from sqlalchemy import Column, String, UUID, CheckConstraint
from sqlalchemy.orm import relationship
from .base_class import BaseClass


class Group(BaseClass):
    __tablename__ = 'group'

    uuid: UUID = Column(UUID, default=uuid4, nullable=False, primary_key=True)
    name: str = Column(String, default="Untitled")

    __table_args__ = (
        CheckConstraint("length(name) <= 128", name="name_length_constraint"),
    )

    complexes = relationship("Complex", back_populates="group", cascade="delete")
