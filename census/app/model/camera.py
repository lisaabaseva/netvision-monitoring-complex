from uuid import uuid4

from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey, UUID, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from .base_class import BaseClass
import re
import logging

logger = logging.getLogger('logger')


class Camera(BaseClass):
    """Класс Camera описывает модель камеры для создания таблицы в БД.
    Имеет валидацию ip.
    """
    __tablename__ = 'camera'

    uuid: UUID = Column(UUID, default=uuid4, nullable=False, primary_key=True)
    id: int = Column(Integer, default=0)
    description: str = Column(String, default="No description")
    url: str = Column(String, default="100")
    status: int = Column(Integer, default=0)
    active: bool = Column(Boolean, default=False)
    complex_uuid: UUID = Column(UUID, ForeignKey("complex.uuid"), nullable=False, index=True)

    __table_args__ = (
        CheckConstraint("length(description) <= 256", name="description_length_constraint"),
    )

    @staticmethod
    def validate_ip(url: str) -> bool:
        pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        return bool(re.match(pattern, url))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        try:
            if not self.validate_ip(self.url):
                raise ValueError("Invalid IP address format")
        except ValueError as e:
            print(f"Error: {e}")
            logger.warning(f"Error: {str(e)}")

    complex = relationship("Complex", back_populates="cameras")
