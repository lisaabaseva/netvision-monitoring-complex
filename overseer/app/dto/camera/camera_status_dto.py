from typing import Dict, Any

from pydantic import BaseModel
from uuid import UUID


class CameraStatusDto(BaseModel):
    id: int
    ip: str
    status: int
    active: bool
