from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import router

from config import FASTAPI_VERSION, FASTAPI_TITLE

app = FastAPI(version=FASTAPI_VERSION, title=FASTAPI_TITLE)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


# @app.get("/health")
# async def root():
#     return {"message": "Sucksex"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)