from fastapi import APIRouter

from schemas.camera import CameraDto, CameraStatusDto
from services.camera_service import get_cameras_info, get_cameras_state

router = APIRouter(prefix="/info")


@router.get("/cameras", response_model=list[CameraDto])
async def get_cameras_info_controller(complex_ip: str,
                                      complex_port: str,
                                      login: str,
                                      password: str) -> list[CameraDto]:
    return await get_cameras_info(complex_ip, complex_port, login, password)


@router.get("/states", response_model=list[CameraStatusDto])
async def get_cameras_state_controller(complex_ip: str,
                                       complex_port: str,
                                       login: str,
                                       password: str) -> list[CameraStatusDto]:
    return await get_cameras_state(complex_ip, complex_port, login, password)
