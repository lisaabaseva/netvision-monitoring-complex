from typing import Any
import requests
import logging

from services import authentication, check_camera_status, get_cameras_response

logger = logging.getLogger('logger')


def get_camera_status_queries(cameras_info: list, complex_ip: str, complex_port: str, access_token: str):
    for camera in cameras_info:
        if camera["active"]:
            camera_status = check_camera_status(complex_ip, complex_port, camera["id"], access_token)
            camera["status"] = camera_status
    return cameras_info


def get_cameras_info(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    result = []

    access_token = authentication(complex_ip, complex_port, login, password)

    if access_token is None:
        logger.warning(f"Couldn't authorize using this url: http://{complex_ip}/api/v1/auth")
        return []

    response = get_cameras_response(complex_ip, complex_port, access_token)

    for camera in response:
        camera_info = {"id": camera["id"],
                       "url": camera["url"],
                       "description": camera["description"],
                       "active": camera["active"],
                       "status": 0}
        result.append(camera_info)

    result = get_camera_status_queries(result, complex_ip, complex_port, access_token)

    return result


def get_cameras_state(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    result = []

    access_token = authentication(complex_ip, complex_port, login, password)

    if access_token is None:
        logger.warning(f"Couldn't authorize using this url: http://{complex_ip}/api/v1/auth")
        return []

    response = get_cameras_response(complex_ip, complex_port, access_token)

    for camera in response:
        camera_info = {"id": camera["id"],
                       "active": camera["active"],
                       "status": 0}
        result.append(camera_info)

    result = get_camera_status_queries(result, complex_ip, complex_port, access_token)

    return result

