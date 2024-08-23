from sched import scheduler

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import camera_controller


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(camera_controller.router)


@app.get("/health")
async def root():
    return {"message": "Sucksex"}


if __name__ == "__main__":
    # if scheduler.state == 0:
    #     pass
    # scheduler.start()

    import uvicorn
    
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)