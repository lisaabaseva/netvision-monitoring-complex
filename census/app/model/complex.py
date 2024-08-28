from uuid import uuid4

from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey, UUID
from sqlalchemy.orm import relationship
from .models import Model


class Complex(Model):
    __tablename__ = 'complex'

    uuid: UUID = Column(UUID, default=uuid4, nullable=False, primary_key=True)
    name: Optional[str] = Column(String, default="")
    ip: Optional[str] = Column(String, default="192.168.0.1")
    port: Optional[int] = Column(Integer, default=80)
    login: Optional[str] = Column(String, default="")
    password: Optional[str] = Column(String, default="")
    group_uuid: UUID = Column(UUID, ForeignKey("group.uuid"), nullable=False, index=True)

    cameras = relationship("Camera", back_populates="complex", cascade="delete")
    group = relationship("Group", back_populates="complexes")