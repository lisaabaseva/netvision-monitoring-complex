import os

OVERSEER_URL = os.environ.get("OVERSEER_URL") or "http://localhost:8001"
CRON_INTERVAL = int(os.environ.get("CRON_INTERVAL") or 5)
MAX_JOBS_INSTANCES = int(os.environ.get("MAX_JOBS_INSTANCES") or 3)

FASTAPI_VERSION = os.environ.get("FASTAPI_VERSION")
FASTAPI_TITLE = os.environ.get("FASTAPI_TITLE")