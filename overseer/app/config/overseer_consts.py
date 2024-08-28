import os


CAMERA_CHECK_PROTOCOL = os.environ.get("CAMERA_CHECK_PROTOCOL") or "http://"
AUTHENTICATION_TIMEOUT = float(os.environ.get("AUTHENTICATION_TIMEOUT") or 3)
CAMERA_CHECK_TIMEOUT = float(os.environ.get("CAMERA_CHECK_TIMEOUT") or 1)
GET_CAMERAS_TIMEOUT = float(os.environ.get("GET_CAMERAS_TIMEOUT") or 3)

FASTAPI_VERSION = os.environ.get("FASTAPI_VERSION")
FASTAPI_TITLE = os.environ.get("FASTAPI_TITLE")
