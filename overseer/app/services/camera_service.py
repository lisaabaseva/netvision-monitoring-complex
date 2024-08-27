from typing import Any, List

import requests, json

from config import CAMERA_CHECK_PROTOCOL, CAMERA_CHECK_TIMEOUT, GET_CAMERAS_TIMEOUT, AUTHENTICATION_TIMEOUT
from config.overseer_log_config import get_default_logger
from shared.camera_status_codes import CameraStatus
from exeption import UnavailableServer

logger = get_default_logger()


def authentication(complex_ip: str, complex_port: str, login: str, password: str) -> str:

    # logger.info("Sending auth request to the address: " + "http://" + complex_ip + ":" + complex_port + "/api/v1/auth")
    auth_response = requests.post("http://" + complex_ip + ":" + complex_port + "/api/v1/auth",
                                  timeout=AUTHENTICATION_TIMEOUT, 
                                  data=json.dumps({"login": login, "password": password}),
                                  headers={"Content-Type": "application/json"})
    
    if auth_response.status_code != 200:
        raise UnavailableServer("Authentification error")
    
    # logger.info("Auth response: " + str(auth_response.status_code) + " : " + auth_response.text)
    access_token = auth_response.json()["access_token"]
    return access_token


def check_camera_status(complex_ip: str, complex_port: str, camera_id: int, access_token: str) -> int:
    logger.info(
        "Sending camera checking request to the address: " + CAMERA_CHECK_PROTOCOL + complex_ip + 
        ":" + complex_port + "/stream/recognition/" + str(camera_id) + "/snapshot")
    camera_status = CameraStatus.BAD.value
    try:
        resp = requests.get(CAMERA_CHECK_PROTOCOL + complex_ip + ":" + complex_port + 
                            "/stream/recognition/" + str(camera_id) + "/snapshot",
                        timeout=CAMERA_CHECK_TIMEOUT,
                        headers={"access-token": access_token, "Content-Type": "application/json"})
        logger.info("Camera check response: " + str(resp.status_code) + " : " + resp.text)

        if resp.status_code == 200:
            camera_status = CameraStatus.OK.value
    except Exception as err:
        logger.warning("Couldn't connect to the " + complex_ip + " - " + str(camera_id) + " due to exception: " + str(err))
    finally:
        return camera_status


def get_cameras_info(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    result = []
    access_token = None
    response = None
    try:
        access_token = authentication(complex_ip, complex_port, login, password)
    except Exception as err:
        logger.warning("Couldn't authorize using this url: " + "http://" + complex_ip + "/api/v1/auth")
        logger.warning("The error message: " + str(err))

    if access_token is None:
        return []

    try:
        response = requests.get("http://" + complex_ip + ":" + complex_port + "/api/v1/cameras",
                            timeout=GET_CAMERAS_TIMEOUT,
                            headers={"access-token": access_token, "Content-Type": "application/json"})

        if response.status_code != 200:
            raise UnavailableServer("Couldn't send camera list request to the census server")

    except Exception as err:
        logger.warning("Couldn't connect to the url: " + "http://" + complex_ip + ":" + complex_port + "/api/v1/cameras")
        logger.warning("The error message: " + str(err))

    if response is None:
        return []

    for camera in response.json():
        camera_info = {"id": camera["id"],
                       "url": camera["url"],
                       "description": camera["description"],
                       "active": camera["active"],
                       "status": 0}
        result.append(camera_info)

    for camera in result:
        if camera["active"]:
            camera_status = check_camera_status(complex_ip, complex_port, camera["id"], access_token)
            camera["status"] = camera_status

    return result


def get_cameras_state(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    result = []
    access_token = None
    response = None
    try:
        access_token = authentication(complex_ip, complex_port, login, password)
    except Exception as err:
        logger.warning("Couldn't authorize using this url: " + "http://" + complex_ip + "/api/v1/auth")
        logger.warning("The error message: " + str(err))

    if access_token is None:
        return []

    try:
        response = requests.get("http://" + complex_ip + ":" + complex_port + "/api/v1/cameras",
                                timeout=GET_CAMERAS_TIMEOUT,
                                headers={"access-token": access_token, "Content-Type": "application/json"})

        if response.status_code != 200:
            raise UnavailableServer("Couldn't send camera list request to the census server")

    except Exception as err:
        logger.warning("Couldn't connect to the url: " + "http://" + complex_ip + ":" + complex_port + "/api/v1/cameras")
        logger.warning("The error message: " + str(err))

    if response is None:
        return []

    for camera in response.json():
        camera_info = {"id": camera["id"],
                       "active": camera["active"],
                       "status": 0}
        result.append(camera_info)

    for camera in result:
        if camera["active"]:
            camera_status = check_camera_status(complex_ip, complex_port, camera["id"], access_token)
            camera["status"] = camera_status

    return result

# complex_url/api/v1/cameras - get cams - [ {"id": num, "url": str, "active": bool, "description": str} ]
# complex_url/stream/recognition/cam_id/snapshot - TIMEOUT 10s
# complex_url/api/v1/traffic-zones/version - { "version": "0.3.15" }

