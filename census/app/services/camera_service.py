import uuid
from typing import List
import requests

from census.app.config.census_consts import OVERSEER_URL
from census.app.exceptions.unavailable_service import UnavailableService
from census.app.services.complex_service import ComplexService
from repository import CameraRepository
from dto.camera import CameraStatesUpdate, CameraCreate
from model import Camera


class CameraService:
    def __init__(self, camera_repository: CameraRepository, complex_service: ComplexService):
        self.camera_repository = camera_repository
        self.complex_service = complex_service


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

        
    def update_cameras_states(self, complex_ip: str, login: str, password: str) -> None:
        url = OVERSEER_URL + "/states/" 
        headers = {
            "ip-complex": complex_ip,
            "login": login,
            "password": password
        } 
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise UnavailableService("Couldn't get cameras states from overseer server")
        
        complex = self.complex_service.get_complex_by_ip(complex_ip)

        cameras_states: List[CameraStatesUpdate] = response.json()
        return self.camera_repository.update_cameras_states(complex.uuid, cameras_states)
    
    
    def get_cameras_info(self, complex_ip: str, login: str, password: str) -> None:
        url = OVERSEER_URL + "/cameras/" 
        headers = {
            "ip-complex": complex_ip,
            "login": login,
            "password": password
        } 
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            raise UnavailableService("Couldn't get cameras states from overseer server")
        
        for camera in response.json:
            self.camera_repository.create_camera(camera)    
        
            