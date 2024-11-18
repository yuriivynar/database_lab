from typing import List

from lab4.app.my_project.auth.dao import access_point_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class AccessPointService(GeneralService):

    _dao = access_point_dao

    def get_access_point_after_brand_id(self, brand_id: int) -> List[object]:
        return self._dao.get_access_point_after_brand_id(brand_id)
