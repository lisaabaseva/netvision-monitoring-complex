from pydantic import BaseModel


class CameraDto(BaseModel):
    """Класс CameraDto - это DTO для приведения данных из ответа на запрос всей информации о камерах
    в формализованный вид.
    """

    id: int
    description: str
    url: str
    active: bool
    status: int


class CameraStatusDto(BaseModel):
    """Класс CameraStatusDto - это DTO для приведения данных из ответа на запрос о состоянии камер
    в формализованный вид.
    """

    id: int
    status: int
    active: bool
