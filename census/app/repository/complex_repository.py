import uuid

from sqlmodel import select
from sqlmodel import Session

from model import Complex
from config.init_db import get_session


class ComplexRepository:
    """Класс ComplexRepository предоставляет набор методов для взаимодействия с моделью комплекса в базе данных."""
    def get_complexes(self) -> list[Complex]:
        """Возвращает список всех комплексов в БД."""
        session: Session = next(get_session())
        result = session.scalars(select(Complex)).all()
        session.close()
        return [Complex(uuid=complex.uuid,
                        name=complex.name,
                        ip=complex.ip,
                        port=complex.port,
                        login=complex.login,
                        password=complex.password,
                        group_uuid=complex.group_uuid) for complex in result]

    def get_complex_by_id(self, complex_id: uuid.UUID) -> Complex:
        """Возвращает из БД комплекс по его id."""
        session: Session = next(get_session())
        result = session.get(Complex, complex_id)
        session.close()
        return result

    def get_complex_by_ip(self, ip: str) -> Complex:
        """Возвращает из БД комплекс по его ip."""
        session: Session = next(get_session())
        result = session.scalars(select(Complex).where(Complex.ip == ip))
        session.close()
        return result

    def create_complex(self, complex_create: Complex) -> Complex:
        """Создает новый комплекс в БД."""
        session: Session = next(get_session())

        session.add(complex_create)
        session.commit()
        session.refresh(complex_create)
        session.close()
        return complex_create

    def delete_complex_by_id(self, complex_id: uuid.UUID) -> bool:
        """Удаляет из БД комплекс по его ID."""
        session: Session = next(get_session())
        result = session.get(Complex, complex_id)

        if result is None:
            return False

        session.delete(result)
        session.commit()
        session.close()
        return True
