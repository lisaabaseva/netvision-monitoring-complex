from typing import Dict, Any

from pydantic import BaseModel
from uuid import UUID


class CameraStatusDto(BaseModel):
    id: int
    status: int
    active: bool

    def to_dict(self) -> Dict[str, Any]:
        return {"uuid": str(self.uuid), "status": self.status, "active": self.active}
