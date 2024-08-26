from services.camera_service import CameraService
from services.complex_service import ComplexService
from services.group_service import GroupService
from repository import GroupRepository, ComplexRepository, CameraRepository

groupRepository: GroupRepository = GroupRepository()
complexRepository: ComplexRepository = ComplexRepository()
cameraRepository: CameraRepository = CameraRepository()


def get_group_service() -> GroupService:
    return GroupService(groupRepository)


def get_complex_service() -> ComplexService:
    return ComplexService(complexRepository)


def get_camera_service() -> CameraService:
    return CameraService(cameraRepository)