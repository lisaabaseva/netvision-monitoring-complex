import uuid

from fastapi import Depends
from typing import List

from sqlmodel import select
from sqlmodel import Session

from census.app.model.camera import Camera
from census.app.dto.camera import StatusesUpdate
from census.app.config.init_db import get_session


class CameraRepository:
    def get_cameras(self) -> List[Camera]:
        session: Session = next(get_session())
        result = session.scalars(select(Camera)).all()
        session.close()
        return [Camera(uuid=camera.uuid,
                       url=camera.url,
                       id=camera.id,
                       description=camera.description,
                       active=camera.active,
                       status=camera.status,
                       complex_uuid=camera.complex_uuid) for camera in result]

    def get_camera_by_id(self, camera_id: uuid.UUID) -> Camera:
        session: Session = next(get_session())
        result = session.get(Camera, camera_id)
        session.close()
        return result

    def create_camera(self, camera_create: Camera) -> Camera:
        session: Session = next(get_session())
        new_camera = Camera(description=camera_create.description,
                            url=camera_create.url,
                            id=camera_create.id,
                            status=camera_create.status,
                            active=camera_create.active,
                            complex_uuid=camera_create.complex_uuid)

        session.add(new_camera)
        session.commit()
        session.refresh(new_camera)
        session.close()

        return new_camera

    def delete_camera_by_id(self, camera_id: uuid.UUID) -> bool:
        session: Session = next(get_session())
        result = session.get(Camera, camera_id)

        if result is None:
            return False

        session.delete(result)
        session.commit()
        session.close()
        return True

    def update_cameras_statuses(self, cameras_to_statuses: List[StatusesUpdate]) -> None:
        session: Session = next(get_session())
        for pair in cameras_to_statuses:
            camera = session.get(Camera, pair.uuid)
            camera.status = pair.status
            session.commit()
        session.close()