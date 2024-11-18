from typing import List
from lab4.app.my_project.auth.dao import monitor_in_workplace_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class MonitorInWorkplaceService(GeneralService):

    _dao = monitor_in_workplace_dao

    def get_monitor_after_workplace(self, workplace_id: int) -> List[object]:
        return self._dao.get_monitor_after_workplace(workplace_id)

    def get_workplace_after_monitor(self, monitor_id: int) -> List[object]:
        return self._dao.get_workplace_after_monitor(monitor_id)