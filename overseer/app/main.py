from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)
