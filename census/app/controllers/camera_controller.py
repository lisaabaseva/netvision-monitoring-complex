from fastapi import APIRouter, Depends
from typing import List

import uuid

from depends import get_camera_service
from dto.camera import CameraOut, CameraCreate, CameraStatesUpdate
from model import Camera
from services.camera_service import CameraService


router = APIRouter(prefix="/cameras")


@router.get("/", response_model=List[CameraOut])
async def get_all_cameras(service: CameraService = Depends(get_camera_service)) -> List[Camera]:
    return service.get_cameras_response()


@router.get("/{camera_id}", response_model=CameraOut)
async def get_camera(camera_id: uuid.UUID, service: CameraService = Depends(get_camera_service)) -> Camera:
    return service.get_camera_by_id(camera_id)


@router.post("/", response_model=CameraOut)
async def create_camera(camera_create: CameraCreate, service: CameraService = Depends(get_camera_service)) -> Camera:
    return service.create_camera(camera_create)


@router.delete("/{camera_id}")
async def delete_camera(camera_id: uuid.UUID, service: CameraService = Depends(get_camera_service)) -> bool:
    return service.delete_camera_by_id(camera_id)
