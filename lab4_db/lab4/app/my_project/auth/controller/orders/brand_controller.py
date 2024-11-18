from lab4.app.my_project.auth.service import brand_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class BrandController(GeneralController):
    _service = brand_service

