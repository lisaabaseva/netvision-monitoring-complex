from fastapi import APIRouter, Depends
from typing import List

import uuid
from dto.camera import CameraDto, CameraStatusDto
from services.camera_service import get_cameras_info, get_cameras_state

router = APIRouter(prefix="/info")


@router.get("/cameras/", response_model=List[CameraDto])
async def get_cameras_info(complex_ip: str, login: str, password: str) -> List[CameraDto]:
    return get_cameras_info(complex_ip, login, password)


@router.get("/states/", response_model=List[CameraStatusDto])
async def get_cameras_state(complex_ip: str, login: str, password: str) -> List[CameraStatusDto]:
    return get_cameras_state(complex_ip, login, password)
