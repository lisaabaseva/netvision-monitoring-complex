import uuid

from typing import List

from sqlmodel import select
from sqlmodel import Session

from dto.complex import ComplexCreate
from model import Complex
from config.init_db import get_session


class ComplexRepository:
    def get_complexes(self) -> List[Complex]:
        session: Session = next(get_session())
        result = session.scalars(select(Complex)).all()
        session.close()
        return [Complex(uuid=camera.uuid,
                        name=camera.name,
                        ip=camera.ip,
                        port=camera.port,
                        login=camera.login,
                        password=camera.password,
                        group_uuid=camera.group_uuid) for camera in result]

    def get_complex_by_id(self, complex_id: uuid.UUID) -> Complex:
        session: Session = next(get_session())
        result = session.get(Complex, complex_id)
        session.close()
        return result

    def create_complex(self, complex_create: Complex) -> Complex:
        session: Session = next(get_session())

        session.add(complex_create)
        session.commit()
        session.refresh(complex_create)
        session.close()

        return complex_create

    def delete_complex_by_id(self, complex_id: uuid.UUID) -> bool:
        session: Session = next(get_session())
        result = session.get(Complex, complex_id)

        if result is None:
            return False

        session.delete(result)
        session.commit()
        session.close()
        return True