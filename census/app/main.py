from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apscheduler.schedulers.background import BackgroundScheduler

from config.init_db import init_db
from config import Config

from controllers import camera_controller, complex_controller, group_controller
from model.complex import Complex
from depends import get_camera_service, get_complex_service


app = FastAPI(version=Config.FASTAPI_VERSION, title=Config.FASTAPI_TITLE)

origins = [Config.FRONTEND_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
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
        get_camera_service().update_cameras_states(complex.ip, complex.port, complex.login, complex.password, complex.uuid)


scheduler = BackgroundScheduler(job_defaults={'max_instances': Config.MAX_JOBS_INSTANCES})
scheduler.add_job(update_all_cameras, 'interval', seconds=Config.CRON_INTERVAL)


@app.on_event("startup")
def on_startup():
    init_db()
    

if __name__ == "__main__":
    import uvicorn
    
    if scheduler.state == 0:
        pass
    scheduler.start()

    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)


