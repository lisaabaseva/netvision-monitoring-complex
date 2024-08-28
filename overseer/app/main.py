from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gunicorn.app.base import BaseApplication
import multiprocessing
import uvicorn
import os

from routers import router
from config import Config

app = FastAPI(version=Config.VERSION, title=Config.TITLE)

origins = [Config.CENSUS_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


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

    if Config.SERVER == "gunicorn":
        options = {
            "bind": "%s:%s" % ("0.0.0.0", "8001"),
            "workers": number_of_workers(),
            "worker_class": "uvicorn.workers.UvicornWorker",
        }
        StandaloneApplication(app, options).run()
    else:
        uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)
