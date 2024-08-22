from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.init_db import init_db

from controllers.routes import camera, group, complex

from cron.jobs import scheduler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(camera.router)
app.include_router(group.router)
app.include_router(camera.router_statuses)
app.include_router(complex.router)


@app.on_event("startup")
def on_startup():
    init_db()


if __name__ == "__main__":
    import uvicorn

    if scheduler.state == 0:
        pass
    scheduler.start()


    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)


