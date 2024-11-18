from lab4.app.my_project.auth.service import position_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PositionController(GeneralController):
    _service = position_service

