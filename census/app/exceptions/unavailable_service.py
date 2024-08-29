class UnavailableService(Exception):
    """UnavailableService - это пользовательский класс, который используется для указания на недоступность сервиса."""
    def __init__(self, msg):
        super().__init__(msg)
