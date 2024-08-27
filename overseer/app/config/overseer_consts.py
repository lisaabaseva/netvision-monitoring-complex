import os

CAMERA_CHECK_PROTOCOL = os.environ.get("CAMERA_CHECK_PROTOCOL") or "http://"
CAMERA_CHECK_TIMEOUT = float(os.environ.get("CAMERA_CHECK_TIMEOUT") or 1)