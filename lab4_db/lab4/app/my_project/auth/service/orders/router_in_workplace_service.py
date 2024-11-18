from typing import List
from lab4.app.my_project.auth.dao import router_in_workplace_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RouterInWorkplaceService(GeneralService):

    _dao = router_in_workplace_dao

    def get_router_after_workplace(self, workplace_id: int) -> List[object]:
        return self._dao.get_router_after_workplace(workplace_id)

    def get_workplace_after_router(self, router_id: int) -> List[object]:
        return self._dao.get_workplace_after_router(router_id)