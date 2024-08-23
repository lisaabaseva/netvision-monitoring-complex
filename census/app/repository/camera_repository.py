import uuid

from fastapi import Depends
from typing import List

from sqlmodel import select
from sqlmodel import Session

from census.app.model.camera import Camera
from census.app.dto.camera import CameraStatesUpdate
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


    def update_cameras_states(self, complex_uuid: uuid, updated_states: List[CameraStatesUpdate]) -> None:
        session: Session = next(get_session())
        for data in updated_states:
            camera = session.scalars(select(Camera).where(Camera.complex_uuid == complex_uuid).where(Camera.id == data.camera_id))
            if camera is None:
                continue
            
            camera.status = data.status
            camera.active = data.active
            session.commit()
        session.close()
        
    
    def get_cameras_id(self) -> List[int]:
        session: Session = next(get_session())
        result = session.scalars(select(Camera)).all()
        session.close()
        return [camera.id for camera in result]
