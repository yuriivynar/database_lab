from typing import List
from lab4.app.my_project.auth.service import monitor_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class MonitorController(GeneralController):
    _service = monitor_service

    def get_monitor_after_brand_id(self, brand_id: int) -> List[object]:
        return self._service.get_monitor_after_brand_id(brand_id)

