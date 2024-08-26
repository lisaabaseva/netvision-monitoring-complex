from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from apscheduler.schedulers.background import BackgroundScheduler

from config.init_db import init_db
from config.census_consts import CRON_INTERVAL, MAX_JOBS_INSTANCES

from controllers import camera_controller, complex_controller, group_controller
from services.camera_service import CameraService
from services.complex_service import ComplexService
from model.complex import Complex
from depends import get_camera_service, get_complex_service

from typing import List


app = FastAPI()

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
    complexes: List[Complex] = get_complex_service().get_complexes()
    for complex in complexes:
        get_camera_service().update_cameras_states(complex.ip, complex.port, complex.login, complex.password, complex.uuid)


scheduler = BackgroundScheduler(job_defaults={'max_instances': MAX_JOBS_INSTANCES})
scheduler.add_job(update_all_cameras, 'interval', seconds=CRON_INTERVAL)


@app.on_event("startup")
def on_startup():
    init_db()
    

if __name__ == "__main__":
    import uvicorn
    
    if scheduler.state == 0:
        pass
    scheduler.start()

    uvicorn.run("main:app", reload=True, host="localhost", port=8000)


