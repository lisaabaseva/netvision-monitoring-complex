from typing import Dict, Any

from pydantic import BaseModel
from uuid import UUID


class CameraStatusOut(BaseModel):
    uuid: UUID
    id: int
    status: int

    def to_dict(self) -> Dict[str, Any]:
        return {"uuid": str(self.uuid), "status": self.status}