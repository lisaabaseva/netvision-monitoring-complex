from typing import Any
import aiohttp
import logging

from services import authentication, check_camera_status, get_cameras_response
from schemas.camera import CameraStatusDto, CameraDto

logger = logging.getLogger('logger')


async def get_camera_status_queries(session, cameras_info: list, complex_ip: str, complex_port: str, access_token: str):
    """Функция для получения статусов всех активных камер."""
    for camera in cameras_info:
        if camera.active:
            camera_status = await check_camera_status(session, complex_ip, complex_port, camera.id, access_token)
            camera.status = camera_status
    return cameras_info


async def get_cameras_info(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    """Функция для получения общей информации о камерах."""
    result = []

    async with aiohttp.ClientSession() as session:
        access_token = await authentication(session, complex_ip, complex_port, login, password)

        if access_token is None:
            logger.warning(f"Couldn't authorize using this url: http://{complex_ip}/api/v1/auth")
            return []

        response: list[dict] = await get_cameras_response(session, complex_ip, complex_port, access_token)

        for camera in response:
            camera_info = CameraDto(
                id=camera.get("id"),
                url=camera.get("url"),
                description=camera.get("description"),
                active=camera.get("active"),
                status=0)
            result.append(camera_info)

        result = await get_camera_status_queries(session, result, complex_ip, complex_port, access_token)

    return result


async def get_cameras_state(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    """Функция для получения информации о активности и статусе всех камер."""
    result = []

    async with aiohttp.ClientSession() as session:

        access_token = await authentication(session, complex_ip, complex_port, login, password)

        if access_token is None:
            logger.warning(f"Couldn't authorize using this url: http://{complex_ip}/api/v1/auth")
            return []

        response: list[dict] = await get_cameras_response(session, complex_ip, complex_port, access_token)

        for camera in response:
            camera_info = CameraStatusDto(
                id=camera.get("id"),
                active=camera.get("active"),
                status=0
                )
            result.append(camera_info)

        result = await get_camera_status_queries(session, result, complex_ip, complex_port, access_token)

    return result
