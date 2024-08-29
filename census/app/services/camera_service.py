import uuid
import requests

from config import Config
from exceptions.unavailable_service import UnavailableService
from repository import CameraRepository
from dto.camera import CameraStatesUpdate, CameraCreate
from model import Camera

config = Config()

class CameraService:
    def __init__(self, camera_repository: CameraRepository):
        self.camera_repository = camera_repository

    def get_cameras(self) -> list[Camera]:
        return self.camera_repository.get_cameras()

    def get_camera_by_id(self, camera_id: uuid.UUID) -> Camera:
        return self.camera_repository.get_camera_by_id(camera_id)

    def create_camera(self, camera_create: CameraCreate) -> Camera:
        new_camera: Camera = Camera(description=camera_create.description,
                                    id=camera_create.id,
                                    url=camera_create.url,
                                    active=camera_create.active,
                                    status=camera_create.status,
                                    complex_uuid=camera_create.complex_uuid)
        return self.camera_repository.create_camera(new_camera)

    def delete_camera_by_id(self, camera_id: uuid.UUID) -> bool:
        return self.camera_repository.delete_camera_by_id(camera_id)

    def update_cameras_states(self, complex_ip: str, complex_port: int, login: str, password: str,
                              complex_uuid: uuid) -> None:
        url = config.OVERSEER_URL + "/info/states"
        params = {
            "complex_ip": complex_ip,
            "complex_port": complex_port,
            "login": login,
            "password": password
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise UnavailableService("Couldn't get cameras states from overseer server")

        cameras_states: list[CameraStatesUpdate] = response.json()
        return self.camera_repository.update_cameras_states(complex_uuid, cameras_states)

    def fill_camera_repository(self, complex_ip: str, complex_port: str, login: str, password: str,
                               complex_uuid: uuid) -> None:
        url = config.OVERSEER_URL + "/info/cameras"
        params = {
            "complex_ip": complex_ip,
            "complex_port": complex_port,
            "login": login,
            "password": password
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise UnavailableService("Couldn't get cameras states from overseer server")

        for camera in response.json():
            self.camera_repository.create_camera(camera, complex_uuid)
