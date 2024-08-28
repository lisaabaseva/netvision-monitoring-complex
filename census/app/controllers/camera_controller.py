from fastapi import APIRouter, Depends

import uuid

from depends import get_camera_service
from dto.camera import CameraCreate, CameraOut
from model import Camera
from services.camera_service import CameraService


router = APIRouter(prefix="/cameras")


@router.get("/", response_model=list[CameraOut])
async def get_all_cameras(service: CameraService = Depends(get_camera_service)) -> list[Camera]:
    return service.get_cameras()


@router.get("/{camera_id}", response_model=CameraOut)
async def get_camera(camera_id: uuid.UUID, service: CameraService = Depends(get_camera_service)) -> Camera:
    return service.get_camera_by_id(camera_id)


@router.post("/", response_model=CameraOut)
async def create_camera(camera_create: CameraCreate, service: CameraService = Depends(get_camera_service)) -> Camera:
    return service.create_camera(camera_create)


@router.delete("/{camera_id}", response_model=bool)
async def delete_camera(camera_id: uuid.UUID, service: CameraService = Depends(get_camera_service)) -> bool:
    return service.delete_camera_by_id(camera_id)
