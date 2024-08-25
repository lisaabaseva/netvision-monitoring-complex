from typing import Any, List

import requests, json

from config import CENSUS_URL, CAMERA_CHECK_PROTOCOL

from shared.camera_status_codes import CameraStatus

from dto.camera import CameraStatusDto, CameraDto

from exeption import CensusUnavailable
from config import CENSUS_URL, CAMERA_CHECK_TIMEOUT
from config.overseer_log_config import get_default_logger

logger = get_default_logger()


def authentification(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    logger.info("Sending auth request to the address: " + "http://" + complex_ip + ":" + complex_port + "/api/v1/auth")
    auth_response = requests.post("http://" + complex_ip + ":" + complex_port + "/api/v1/auth",
                                  timeout=3, data=json.dumps({"login": login, "password": password}),
                                  headers={"Content-Type": "application/json"})
    
    if auth_response.status_code != 200:
        raise CensusUnavailable("Authentification error")
    logger.info("Auth response: " + str(auth_response.status_code) + " : " + auth_response.text)
    access_token = auth_response.json()["access_token"]
    return access_token


def check_camera_status(camera_ip: str, camera_id: str, access_token: str) -> Any:
    logger.info(
        "Sending camera checking request to the address: " + CAMERA_CHECK_PROTOCOL + camera_ip + "/stream/recognition/" + str(
            camera_id) + "/snapshot")
    resp = requests.get(CAMERA_CHECK_PROTOCOL + camera_ip + "/stream/recognition/" + str(camera_id) + "/snapshot",
                        timeout=CAMERA_CHECK_TIMEOUT,
                        headers={"access-token": access_token, "Content-Type": "application/json"})
    logger.info("Camera check response: " + str(resp.status_code) + " : " + resp.text)

    if resp.status_code == 200:
        return CameraStatus.OK.value
    return CameraStatus.BAD.value


def get_cameras_info(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    result = []
    
    access_token = authentification(complex_ip, complex_port, login, password)
    response = requests.get("http://" + complex_ip + ":" + complex_port + "/api/v1/cameras",
                            timeout=CAMERA_CHECK_TIMEOUT,
                            headers={"access-token": access_token, "Content-Type": "application/json"})

    if response.status_code != 200:
        raise CensusUnavailable("Couldn't send camera list request to the census server")

    for camera in response.json():
        camera_info = {"id": camera["id"],
                       "description": camera["description"],
                       "ip": camera["ip"],
                       "active": camera["active"],
                       "status": 0}
        result.append(camera_info)

    for camera in result:
        if camera["active"]:
            camera_status = check_camera_status(camera["ip"], camera["id"], access_token)
            camera["status"] = camera_status

    return result


def get_cameras_state(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    result = []

    access_token = authentification(complex_ip, complex_port, login, password)
    response = requests.get("http://" + complex_ip + ":" + complex_port + "/api/v1/cameras",
                            timeout=CAMERA_CHECK_TIMEOUT,
                            headers={"access-token": access_token, "Content-Type": "application/json"})

    if response.status_code != 200:
        raise CensusUnavailable("Couldn't send camera list request to the census server")

    for camera in response.json():
        camera_info = {"id": camera["id"],
                       "ip": camera["ip"],
                       "active": camera["active"],
                       "status": 0}
        result.append(camera_info)

    for camera in result:
        if camera["active"]:
            camera_status = check_camera_status(camera["ip"], camera["id"], access_token)
            camera["status"] = camera_status
            del camera["ip"]

    return result


def send_statuses(cameras_to_statuses: List[CameraStatusDto]) -> None:
    data_to_send = json.dumps([x.to_dict() for x in cameras_to_statuses])
    logger.info("Sending new statuses with the payload: " + data_to_send)
    response = requests.post(CENSUS_URL + "/statuses/", data=data_to_send)
    if not response.status_code == 200:
        raise CensusUnavailable("Couldn't sent new statuses request to the census server")

# complex_url/api/v1/cameras - get cams - [ {"id": num, "url": str, "active": bool, "description": str} ]
# complex_url/stream/recognition/cam_id/snapshot - TIMEOUT 10s
# complex_url/api/v1/traffic-zones/version - { "version": "0.3.15" }

