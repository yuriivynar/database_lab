from typing import List
from lab4.app.my_project.auth.service import monitor_in_workplace_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class MonitorInWorkplaceController(GeneralController):
    _service = monitor_in_workplace_service

    def get_monitor_after_workplace(self, workplace_id: int) -> List[object]:
        return self._service.get_monitor_after_workplace(workplace_id)

    def get_workplace_after_monitor(self, monitor_id: int) -> List[object]:
        return self._service.get_workplace_after_monitor(monitor_id)

