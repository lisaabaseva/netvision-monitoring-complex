from uuid import uuid4

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from .base_class import BaseClass


class Group(BaseClass):
    __tablename__ = 'group'

    uuid: UUID = Column(UUID, default=uuid4, nullable=False, primary_key=True)
    name: str = Column(String, default="")

    complexes = relationship("Complex", back_populates="group", cascade="delete")
