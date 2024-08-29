from fastapi import APIRouter, Depends

import uuid

from depends import get_group_service
from model import Group
from dto.group import GroupOut, GroupCreate

from services.complex_service import ComplexService
from services.camera_service import CameraService
from services.group_service import GroupService

router = APIRouter(prefix="/groups")


@router.get("/", response_model=list[GroupOut])
async def get_all_groups(service: GroupService = Depends(get_group_service)) -> list[Group]:
    """Возвращает список всех групп."""
    return service.get_groups()


@router.post("/", response_model=GroupOut)
async def create_group(group_create: GroupCreate, service: GroupService = Depends(get_group_service)) -> Group:
    """Создает новую группу."""
    return service.create_group(group_create)


@router.delete("/{group_id}", response_model=bool)
async def delete_group(group_id: uuid.UUID, service: GroupService = Depends(get_group_service)) -> bool:
    """Удаляет группу по ее id."""
    return service.delete_group_by_id(group_id)