from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gunicorn.app.base import BaseApplication
import uvicorn

import multiprocessing
from apscheduler.schedulers.background import BackgroundScheduler

from config.init_db import init_db
from config import Config

from controllers import camera_controller, complex_controller, group_controller
from model.complex import Complex
from depends import get_camera_service, get_complex_service

config = Config()

app = FastAPI(version=config.VERSION, title=config.TITLE)

origins = [config.FRONTEND_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(camera_controller.router)
app.include_router(complex_controller.router)
app.include_router(group_controller.router)


def update_all_cameras():
    complexes: list[Complex] = get_complex_service().get_complexes()
    for complex in complexes:
        get_camera_service().update_cameras_states(complex.ip, complex.port, complex.login, complex.password,
                                                   complex.uuid)


scheduler = BackgroundScheduler(job_defaults={'max_instances': config.MAX_JOBS_INSTANCES})
scheduler.add_job(update_all_cameras, 'interval', seconds=config.CRON_INTERVAL)


@app.on_event("startup")
def on_startup():
    init_db()


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(BaseApplication):
    def __init__(self, application: callable, options: dict[str, any] = None):
        self.options = options or {}
        self.application = application
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == "__main__":

    if scheduler.state == 0:
        pass
    scheduler.start()

    if config.SERVER == "gunicorn":
        options = {
            "bind": "%s:%s" % ("0.0.0.0", "8000"),
            "workers": number_of_workers(),
            "worker_class": "uvicorn.workers.UvicornWorker",
        }
        StandaloneApplication(app, options).run()
    else:
        uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
