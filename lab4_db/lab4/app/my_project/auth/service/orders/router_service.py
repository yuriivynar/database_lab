from typing import List
from lab4.app.my_project.auth.dao import router_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RouterService(GeneralService):

    _dao = router_dao

    def get_router_after_brand_id(self, brand_id: int) -> List[object]:
        return self._dao.get_router_after_brand_id(brand_id)