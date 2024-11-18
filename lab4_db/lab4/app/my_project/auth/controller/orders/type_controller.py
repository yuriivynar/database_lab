from lab4.app.my_project.auth.service import type_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class TypeController(GeneralController):
    _service = type_service

