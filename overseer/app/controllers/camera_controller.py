from fastapi import APIRouter, Depends
from typing import List

import uuid
from dto.camera import CameraDto, CameraStatusDto
from services.camera_service import get_cameras_info, get_cameras_state

router = APIRouter(prefix="/info")


@router.get("/cameras/", response_model=List[CameraDto])
async def get_cameras_info_controller(complex_ip: str, complex_port: str, login: str, password: str) -> List[CameraDto]:
    return get_cameras_info(complex_ip, complex_port, login, password)


@router.get("/states/", response_model=List[CameraStatusDto])
async def get_cameras_state_controller(complex_ip: str, complex_port: str, login: str, password: str) -> List[CameraStatusDto]:
    return get_cameras_state(complex_ip, complex_port, login, password)
