from typing import List
from lab4.app.my_project.auth.dao import access_point_in_workplace_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class AccessPointInWorkplaceService(GeneralService):

    _dao = access_point_in_workplace_dao

    def get_access_point_after_workplace(self, workplace_id: int) -> List[object]:
        return self._dao.get_access_point_after_workplace(workplace_id)

    def get_workplace_after_access_point(self, access_point_id: int) -> List[object]:
        return self._dao.get_workplace_after_access_point(access_point_id)