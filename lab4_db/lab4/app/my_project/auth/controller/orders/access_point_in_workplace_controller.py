from typing import List
from lab4.app.my_project.auth.service import access_point_in_workplace_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class AccessPointInWorkplaceController(GeneralController):
    _service = access_point_in_workplace_service

    def get_access_point_after_workplace(self, workplace_id: int) -> List[object]:
        return self._service.get_access_point_after_workplace(workplace_id)

    def get_workplace_after_access_point(self, access_point_id: int) -> List[object]:
        return self._service.get_workplace_after_access_point(access_point_id)


