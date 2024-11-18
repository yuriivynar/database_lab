from typing import List
from lab4.app.my_project.auth.dao import ip_phone_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class IpPhoneService(GeneralService):

    _dao = ip_phone_dao

    def get_ip_phone_after_brand_id(self, brand_id: int) -> List[object]:
        return self._dao.get_ip_phone_after_brand_id(brand_id)