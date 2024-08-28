from pydantic import BaseModel


class CameraStatesUpdate(BaseModel):
    camera_id: int
    status: int
    active: bool
