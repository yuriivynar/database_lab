from lab4.app.my_project.auth.service import location_type_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class LocationTypeController(GeneralController):
    _service = location_type_service

