from uuid import uuid4

from sqlalchemy import Column, Integer, String, ForeignKey, UUID, CheckConstraint
from sqlalchemy.orm import relationship
from .base_class import BaseClass
import re
import logging

logger = logging.getLogger('logger')


class Complex(BaseClass):
    """Класс Complex описывает модель комплекса для создания таблицы в БД.
    Имеет валидацию ip, ограничение названия комплекса, логина и пароля.
    """

    __tablename__ = 'complex'

    uuid: UUID = Column(UUID, default=uuid4, nullable=False, primary_key=True)
    name: str = Column(String, default="Untitled", nullable=False)
    ip: str = Column(String, default="100", nullable=False)
    port: int = Column(Integer, default=80, nullable=False)
    login: str = Column(String, default="login", nullable=False)
    password: str = Column(String, default="password", nullable=False)
    group_uuid: UUID = Column(UUID, ForeignKey("group.uuid"), nullable=False, index=True)

    __table_args__ = (
        CheckConstraint("length(name) <= 64", name="name_length_constraint"),
        CheckConstraint("port > 0 AND port < 65536", name="valid_port_range"),
        CheckConstraint("length(login) <= 32", name="login_length_constraint"),
        CheckConstraint("length(password) <= 32", name="password_length_constraint"),
    )

    @staticmethod
    def validate_ip(ip: str) -> bool:
        pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        return bool(re.match(pattern, ip))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        try:
            if not self.validate_ip(self.ip):
                raise ValueError("Invalid IP address format")
        except ValueError as e:
            print(f"Error: {e}")
            logger.warning(f"Error: {str(e)}")

    cameras = relationship("Camera", back_populates="complex", cascade="delete")
    group = relationship("Group", back_populates="complexes")
