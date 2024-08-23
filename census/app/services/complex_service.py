import uuid, requests, json
from typing import List

from census.app.repository.complex_repository import ComplexRepository
from census.app.dto.complex import ComplexCreate
from census.app.dto.camera import CameraCreate
from census.app.model.camera import Camera
from census.app.model.complex import Complex
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
    
    
    def get_complex_by_ip(self, complex_ip: str) -> Complex:
        return self.complex_repository.get_complex_by_ip(complex_ip)


    def create_complex(self, complex_create: ComplexCreate) -> Complex:
        new_complex: Complex = Complex(name=complex_create.name,
                                       ip=complex_create.ip,
                                       port=complex_create.port,
                                       login=complex_create.login,
                                       password=complex_create.password,
                                       group_uuid=complex_create.group_uuid)
        
        return self.complex_repository.create_complex(new_complex)


    def delete_complex_by_id(self, complex_id: uuid.UUID) -> bool:
        return self.complex_repository.delete_complex_by_id(complex_id)


# complex_url/api/v1/cameras - get cams - [ {"id": num, "url": str, "active": bool, "description": str} ]
# complex_url/stream/recognition/cam_id/snapshot - TIMEOUT 10s
# complex_url/api/v1/traffic-zones/version - { "version": "0.3.15" }