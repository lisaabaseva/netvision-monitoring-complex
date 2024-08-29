from typing import Any
import logging

import orjson
from aiohttp import ClientError
from config import Config
from shared.camera_status_codes import CameraStatus
from exeption import UnavailableServer

logger = logging.getLogger('logger')
config = Config()


async def authentication(session, complex_ip: str, complex_port: str, login: str, password: str) -> Any:
    try:
        async with session.post(f"http://{complex_ip}:{complex_port}/api/v1/auth",
                                timeout=config.AUTHENTICATION_TIMEOUT,
                                data=orjson.dumps({"login": login, "password": password}),
                                headers={"Content-Type": "application/json"}) as response:
            if response.status != 200:
                raise UnavailableServer("Authentication error")

            auth_response: dict = await response.json()
            return auth_response.get("access_token")

    except UnavailableServer as e:
        logger.warning(f"Failed to retrieve access_token: {str(e)}")
    except ClientError as e:
        logger.warning(f"Couldn't connect to the url: http://{complex_ip}:{complex_port}/api/v1/auth")
        logger.warning(f"The error message: {str(e)}")
    except Exception as e:
        logger.warning(f"Unexpected error occurred: {str(e)}")

    return None


async def check_camera_status(session, complex_ip: str, complex_port: str, camera_id: int, access_token: str) -> int:
    camera_status = CameraStatus.BAD.value

    try:
        async with session.get(
                f"{config.CAMERA_CHECK_PROTOCOL}{complex_ip}:{complex_port}/stream/recognition/{camera_id}/snapshot",
                timeout=config.CAMERA_CHECK_TIMEOUT,
                headers={"access-token": access_token, "Content-Type": "application/json"}) as response:

            if response.status == 200:
                camera_status = CameraStatus.OK.value

    except Exception as e:
        logger.warning(f"Couldn't connect to the {complex_ip} - {camera_id} due to exception: {str(e)}")

    return camera_status


async def get_cameras_response(session, complex_ip: str, complex_port: str, access_token: str) -> Any:
    response = None
    try:
        async with session.get(f"http://{complex_ip}:{complex_port}/api/v1/cameras",
                               timeout=config.GET_CAMERAS_TIMEOUT,
                               headers={"access-token": access_token, "Content-Type": "application/json"}) as response:

            if response.status != 200:
                raise UnavailableServer("Couldn't send camera list request to the census server")

            return await response.json()

    except UnavailableServer as e:
        logger.warning(f"Couldn't send camera list request to the census server: {str(e)}")
    except ClientError as e:
        logger.warning(f"Couldn't connect to the url: http://{complex_ip}:{complex_port}/api/v1/cameras")
        logger.warning(f"The error message: {str(e)}")
    except Exception as e:
        logger.warning(f"Unexpected error occurred: {str(e)}")

    return []
