from typing import List
from lab4.app.my_project.auth.dao import monitor_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class MonitorService(GeneralService):

    _dao = monitor_dao

    def get_monitor_after_brand_id(self, brand_id: int) -> List[object]:
        return self._dao.get_monitor_after_brand_id(brand_id)