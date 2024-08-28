from uuid import uuid4

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


class Group(DeclarativeBase):
    __tablename__ = 'group'

    uuid: UUID = Column(UUID, default=uuid4, nullable=False, primary_key=True)
    name: str = Column(String, default="")

    complexes = relationship("Complex", back_populates="group", cascade="delete")
