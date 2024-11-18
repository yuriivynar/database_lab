from lab4.app.my_project.auth.service import address_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class AddressController(GeneralController):
    _service = address_service

