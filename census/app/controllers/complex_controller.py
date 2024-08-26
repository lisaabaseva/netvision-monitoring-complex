from fastapi import APIRouter, Depends
from typing import List

import uuid

from depends import get_complex_service, get_camera_service
from dto.complex import ComplexDetailedOut, ComplexCreate
from model import Complex
from services.complex_service import ComplexService
from services.camera_service import CameraService

router = APIRouter(prefix="/complexes")


@router.get("/", response_model=List[ComplexDetailedOut])
async def get_all_complexes(service: ComplexService = Depends(get_complex_service)) -> List[Complex]:
    return service.get_complexes()


@router.get("/{complex_id}", response_model=ComplexDetailedOut)
async def get_complex(complex_id: uuid.UUID, service: ComplexService = Depends(get_complex_service)) -> Complex:
    return service.get_complex_by_id(complex_id)


@router.post("/", response_model=ComplexCreate)
async def create_complex(complex_create: ComplexCreate, service: ComplexService = Depends(get_complex_service),
                         camera_service: CameraService = Depends(get_camera_service)) -> Complex:
    created_complex = service.create_complex(complex_create)
    
    camera_service.fill_camera_repository(created_complex.ip, created_complex.port, created_complex.login, created_complex.password, created_complex.uuid)

    return created_complex


@router.delete("/{complex_id}")
async def delete_complex(complex_id: uuid.UUID, service: ComplexService = Depends(get_complex_service)) -> bool:
    return service.delete_complex_by_id(complex_id)