from typing import List
from lab4.app.my_project.auth.dao import ip_phone_in_workplace_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class IpPhoneInWorkplaceService(GeneralService):

    _dao = ip_phone_in_workplace_dao

    def get_ip_phone_after_workplace(self, workplace_id: int) -> List[object]:
        return self._dao.get_ip_phone_after_workplace(workplace_id)

    def get_workplace_after_ip_phone(self, ip_phone_id: int) -> List[object]:
        return self._dao.get_workplace_after_ip_phone(ip_phone_id)