import uuid, requests, json
from typing import List

from census.app.repository import ComplexRepository
from census.app.dto.camera import CameraCreate
from census.app.dto.complex import ComplexCreate
from census.app.model import Complex, Camera
from census.app.services import CameraService

from census.app.config.census_log_config import get_default_logger


class ComplexService:
    def __init__(self, complex_repository: ComplexRepository):
        self.complex_repository = complex_repository
        self.logger = get_default_logger()

    def get_complexes(self) -> List[Complex]:
        return self.complex_repository.get_complexes()

    def get_complex_by_id(self, complex_id: uuid.UUID) -> Complex:
        return self.complex_repository.get_complex_by_id(complex_id)

    def create_complex(self, complex_create: ComplexCreate) -> Complex:
        new_complex: Complex = Complex(name=complex_create.name,
                                       ip=complex_create.ip,
                                       port=complex_create.port,
                                       login=complex_create.login,
                                       password=complex_create.password,
                                       group_uuid=complex_create.group_uuid)

        try:
            self.logger.info("Sending auth request to the address: " + "http://" + new_complex.ip + ":" + str(
                new_complex.port) + "/api/v1/auth")
            auth_response = requests.post("http://" + new_complex.ip + ":" + str(new_complex.port) + "/api/v1/auth",
                                          timeout=3, headers={"Content-Type": "application/json"},
                                          data=json.dumps(
                                              {"login": new_complex.login, "password": new_complex.password}))
            self.logger.info("Auth response: " + str(auth_response.status_code) + " : " + auth_response.text)
            access_token = auth_response.json()["access_token"]

            self.logger.info("Sending version request to the address: " + "http://" + new_complex.ip + ":" + str(
                new_complex.port) + "/api/v1/traffic-zones/version")
            response = requests.get(
                "http://" + new_complex.ip + ":" + str(new_complex.port) + "/api/v1/traffic-zones/version",
                timeout=3, headers={"access-token": access_token, "Content-Type": "application/json"})
            self.logger.info("Version response: " + str(response.status_code) + " : " + response.text)
            version = response.json()["version"]
        except Exception as err:
            self.logger.error("Couldn't sent request to get version. Error msg: " + str(err))
            version = "0.0.1"

        new_complex.version = version

        return self.complex_repository.create_complex(new_complex)

    def create_cameras_in_complex(self, created_complex: Complex, camera_service: CameraService):
        cameras_data = self.__get_complex_data(created_complex)
        self.logger.info("Adding cameras: " + str(cameras_data))
        for camera in cameras_data:
            self.logger.info("Adding camera: " + str(camera.model_dump()))
            camera_service.create_camera(camera)

    def delete_complex_by_id(self, complex_id: uuid.UUID) -> bool:
        return self.complex_repository.delete_complex_by_id(complex_id)

    def __get_complex_data(self, complex: Complex):
        try:
            self.logger.info("Sending auth request to the address: " + "http://" + complex.ip + ":" + str(
                complex.port) + "/api/v1/auth")
            auth_response = requests.post("http://" + complex.ip + ":" + str(complex.port) + "/api/v1/auth", timeout=3,
                                          data=json.dumps({"login": complex.login, "password": complex.password}),
                                          headers={"Content-Type": "application/json"})
            self.logger.info("Auth response: " + str(auth_response.status_code) + " : " + auth_response.text)
            access_token = auth_response.json()["access_token"]

            self.logger.info("Sending complex data request to the address: " + "http://" + complex.ip + ":" + str(
                complex.port) + "/api/v1/cameras")
            response = requests.get("http://" + complex.ip + ":" + str(complex.port) + "/api/v1/cameras",
                                    timeout=3,
                                    headers={"access-token": access_token, "Content-Type": "application/json"})
            self.logger.info("Complex data: " + str(response.status_code) + " : " + response.text)
        except Exception as err:
            self.logger.error("Couldn't fetch complex data due to the error: " + str(err))
            return []

        if response.status_code != 200:
            self.logger.error(
                "Couldn't fetch complex data: " + str(response.json()) + " - " + str(response.status_code))
            return []

        cameras_list = response.json()

        result: List[CameraCreate] = []
        for camera in cameras_list:
            new_camera: CameraCreate = CameraCreate(id=camera["id"],
                                                    description=camera["description"],
                                                    active=camera["active"],
                                                    url=camera["url"],
                                                    complex_uuid=complex.uuid)
            result.append(new_camera)

        return result

# complex_url/api/v1/cameras - get cams - [ {"id": num, "url": str, "active": bool, "description": str} ]
# complex_url/stream/recognition/cam_id/snapshot - TIMEOUT 10s
# complex_url/api/v1/traffic-zones/version - { "version": "0.3.15" }