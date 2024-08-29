from uuid import uuid4

from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey, UUID, Boolean
from sqlalchemy.orm import relationship
from .base_class import BaseClass


class Camera(BaseClass):
    __tablename__ = 'camera'

    uuid: UUID = Column(UUID, default=uuid4, nullable=False, primary_key=True)
    id: Optional[int] = Column(Integer, default=0)
    description: Optional[str] = Column(String, default="")
    url: Optional[str] = Column(String, default="192.168.0.1")
    status: Optional[int] = Column(Integer, default=0)
    active: Optional[bool] = Column(Boolean, default=False)
    complex_uuid: UUID = Column(UUID, ForeignKey("complex.uuid"), nullable=False, index=True)

    complex = relationship("Complex", back_populates="cameras")
