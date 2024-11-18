from typing import List
from lab4.app.my_project.auth.service import ip_phone_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class IpPhoneController(GeneralController):
    _service = ip_phone_service

    def get_ip_phone_after_brand_id(self, brand_id: int) -> List[object]:
        return self._service.get_ip_phone_after_brand_id(brand_id)

