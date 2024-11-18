from typing import List
from lab4.app.my_project.auth.service import access_point_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class AccessPointController(GeneralController):
    _service = access_point_service

    def get_access_point_after_brand_id(self, brand_id: int) -> List[object]:
        return self._service.get_access_point_after_brand_id(brand_id)

