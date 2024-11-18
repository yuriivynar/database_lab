from typing import List
from lab4.app.my_project.auth.service import computer_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ComputerController(GeneralController):
    _service = computer_service

    def get_computer_after_brand_id(self, brand_id: int) -> List[object]:
        return self._service.get_computer_after_brand_id(brand_id)

