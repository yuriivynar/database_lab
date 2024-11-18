from typing import List, Dict, Any
from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import MonitorInWorkplace
import sqlalchemy


class MonitorInWorkplaceDAO(GeneralDAO):
    _domain_type = MonitorInWorkplace

    def get_monitor_after_workplace(self, workplace_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_monitor_after_workplace(:p1)"),
                                       {"p1": workplace_id}).mappings().all()
        return [dict(row) for row in result]

    def get_workplace_after_monitor(self, monitor_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_workplace_after_monitor(:p1)"),
                                       {'p1': monitor_id}).mappings().all()
        return [dict(row) for row in result]