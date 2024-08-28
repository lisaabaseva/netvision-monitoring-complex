from typing import Any
import logging

import requests, json
from config import Config
from shared.camera_status_codes import CameraStatus
from exeption import UnavailableServer

logger = logging.getLogger('logger')


def authentication(complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    try:
        auth_response = requests.post("http://" + complex_ip + ":" + complex_port + "/api/v1/auth",
                                      timeout=Config.AUTHENTICATION_TIMEOUT,
                                      data=json.dumps({"login": login, "password": password}),
                                      headers={"Content-Type": "application/json"})

        if auth_response.status_code != 200:
            raise UnavailableServer("Authentication error")

    except UnavailableServer as e:
        logger.warning(f"Failed to retrieve access_token: {str(e)}")
    except requests.RequestException as e:
        logger.warning(f"Couldn't connect to the url: http://{complex_ip}:{complex_port}/api/v1/auth")
        logger.warning(f"The error message: {str(e)}")
    except Exception as e:
        logger.warning(f"Unexpected error occurred: {str(e)}")

    finally:
        return auth_response.json()["access_token"] if auth_response and auth_response.status_code == 200 else None


def check_camera_status(complex_ip: str, complex_port: str, camera_id: int, access_token: str) -> int:
    camera_status = CameraStatus.BAD.value

    try:
        resp = requests.get(Config.CAMERA_CHECK_PROTOCOL + complex_ip + ":" + complex_port +
                            "/stream/recognition/" + str(camera_id) + "/snapshot",
                            timeout=Config.CAMERA_CHECK_TIMEOUT,
                            headers={"access-token": access_token, "Content-Type": "application/json"})
        logger.info("Camera check response: " + str(resp.status_code) + " : " + resp.text)

        if resp.status_code == 200:
            camera_status = CameraStatus.OK.value

    except Exception as e:
        logger.warning(
            "Couldn't connect to the " + complex_ip + " - " + str(camera_id) + " due to exception: " + str(e))
    finally:
        return camera_status


def get_cameras_response(complex_ip: str, complex_port: str, access_token: str) -> Any:
    response = None
    try:
        response = requests.get("http://" + complex_ip + ":" + complex_port + "/api/v1/cameras",
                                timeout=Config.GET_CAMERAS_TIMEOUT,
                                headers={"access-token": access_token, "Content-Type": "application/json"})

        if response.status_code != 200:
            raise UnavailableServer("Couldn't send camera list request to the census server")

    except UnavailableServer as e:
        logger.warning(f"Couldn't send camera list request to the census server: {str(e)}")
    except requests.RequestException as e:
        logger.warning(f"Couldn't connect to the url: http://{complex_ip}:{complex_port}/api/v1/cameras")
        logger.warning(f"The error message: {str(e)}")
    except Exception as e:
        logger.warning(f"Unexpected error occurred: {str(e)}")

    return response.json() if response and response.status_code == 200 else []

