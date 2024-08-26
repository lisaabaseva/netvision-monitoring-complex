import os

CRON_INTERVAL = int(os.environ.get("CRON_INTERVAL") or 5)
MAX_JOBS_INSTANCES = int(os.environ.get("MAX_JOBS_INSTANCES") or 3)

CAMERA_CHECK_PROTOCOL = os.environ.get("CAMERA_CHECK_PROTOCOL") or "http://"

CAMERA_CHECK_TIMEOUT = int(os.environ.get("CAMERA_CHECK_TIMEOUT") or 3)