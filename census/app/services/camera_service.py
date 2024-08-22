import uuid
from typing import List

from repository import CameraRepository
from dto.camera import StatusesUpdate, CameraCreate
from model import Camera


class CameraService:
    def __init__(self, camera_repository: CameraRepository):
        self.camera_repository = camera_repository

    def get_cameras(self) -> List[Camera]:
        return self.camera_repository.get_cameras()

    def get_camera_by_id(self, camera_id: uuid.UUID) -> Camera:
        return self.camera_repository.get_camera_by_id(camera_id)

    def create_camera(self, camera_create: CameraCreate) -> Camera:
        new_camera: Camera = Camera(description=camera_create.description,
                                    id=camera_create.id,
                                    url=camera_create.url,
                                    active=camera_create.active,
                                    complex_uuid=camera_create.complex_uuid)
        return self.camera_repository.create_camera(new_camera)

    def delete_camera_by_id(self, camera_id: uuid.UUID) -> bool:
        return self.camera_repository.delete_camera_by_id(camera_id)

    def update_cameras_statuses(self, cameras_to_statuses: List[StatusesUpdate]) -> None:
        return self.camera_repository.update_cameras_statuses(cameras_to_statuses)