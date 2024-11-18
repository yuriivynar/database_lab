from typing import List

from lab4.app.my_project.auth.service import office_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class OfficeController(GeneralController):
    _service = office_service

    def get_address_after_location_type(self, location_type_id: int) -> List[object]:
        return self._service.get_address_after_location_type(location_type_id)

    def get_location_type_after_address(self, address_id: int) -> List[object]:
        return self._service.get_location_type_after_address(address_id)