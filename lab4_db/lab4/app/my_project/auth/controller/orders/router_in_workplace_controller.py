from typing import List
from lab4.app.my_project.auth.service import router_in_workplace_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class RouterInWorkplaceController(GeneralController):
    _service = router_in_workplace_service

    def get_router_after_workplace(self, workplace_id: int) -> List[object]:
        return self._service.get_router_after_workplace(workplace_id)

    def get_workplace_after_router(self, router_id: int) -> List[object]:
        return self._service.get_workplace_after_router(router_id)
