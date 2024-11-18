from typing import List

from lab4.app.my_project.auth.dao import office_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class OfficeService(GeneralService):

    _dao = office_dao

    def get_address_after_location_type(self, location_type_id: int) -> List[object]:
        return self._dao.get_address_after_location_type(location_type_id)

    def get_location_type_after_address(self, address_id: int) -> List[object]:
        return self._dao.get_location_type_after_address(address_id)