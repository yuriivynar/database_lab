from typing import List
from lab4.app.my_project.auth.service import ip_phone_in_workplace_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class IpPhoneInWorkplaceController(GeneralController):
    _service = ip_phone_in_workplace_service

    def get_ip_phone_after_workplace(self, workplace_id: int) -> List[object]:
        return self._service.get_ip_phone_after_workplace(workplace_id)

    def get_workplace_after_ip_phone(self, ip_phone_id: int) -> List[object]:
        return self._service.get_workplace_after_ip_phone(ip_phone_id)

