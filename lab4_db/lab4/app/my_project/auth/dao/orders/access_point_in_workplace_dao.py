from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import AccessPointInWorkplace


class AccessPointInWorkplaceDAO(GeneralDAO):
    _domain_type = AccessPointInWorkplace

    def get_access_point_after_workplace(self, workplace_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_access_point_after_workplace(:p1)"),
                                       {"p1": workplace_id}).mappings().all()
        return [dict(row) for row in result]

    def get_workplace_after_access_point(self, access_point_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_workplace_after_access_point(:p1)"),
                                       {'p1': access_point_id}).mappings().all()
        return [dict(row) for row in result]
