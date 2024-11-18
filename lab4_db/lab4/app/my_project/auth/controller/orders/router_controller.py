from typing import List
from lab4.app.my_project.auth.service import router_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class RouterController(GeneralController):
    _service = router_service

    def get_router_after_brand_id(self, brand_id: int) -> List[object]:
        return self._service.get_router_after_brand_id(brand_id)

