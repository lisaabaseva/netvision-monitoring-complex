from pydantic import BaseModel


class CameraStatesUpdate(BaseModel):
    """Класс CameraStatesUpdate - это DTO для изменения состояния камеры."""
    camera_id: int
    status: int
    active: bool
