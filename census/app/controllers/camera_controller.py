from fastapi import APIRouter, Depends
from typing import List

import uuid

from depends import get_camera_service
from dto.camera import CameraOut, CameraCreate, StatusesUpdate
from model import Camera
from services import CameraService


router = APIRouter(prefix="/cameras")


@router.get("/", response_model=List[CameraOut])
async def get_all_cameras(service: CameraService = Depends(get_camera_service)) -> List[Camera]:
    return service.get_cameras()


@router.get("/{camera_id}", response_model=CameraOut)
async def get_camera(camera_id: uuid.UUID, service: CameraService = Depends(get_camera_service)) -> Camera:
    return service.get_camera_by_id(camera_id)


@router.post("/", response_model=CameraOut)
async def create_camera(camera_create: CameraCreate, service: CameraService = Depends(get_camera_service)) -> Camera:
    return service.create_camera(camera_create)


@router.delete("/{camera_id}")
async def delete_camera(camera_id: uuid.UUID, service: CameraService = Depends(get_camera_service)) -> bool:
    return service.delete_camera_by_id(camera_id)


router_statuses = APIRouter(prefix="/statuses")


@router_statuses.post("/")
async def update_statuses(cameras_to_statuses: List[StatusesUpdate], service: CameraService = Depends(get_camera_service)) -> None:
    return service.update_cameras_statuses(cameras_to_statuses)