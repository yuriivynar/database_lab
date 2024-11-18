from typing import List, Dict, Any
from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import RouterInWorkplace
import sqlalchemy


class RouterInWorkplaceDAO(GeneralDAO):
    _domain_type = RouterInWorkplace

    def get_router_after_workplace(self, workplace_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_router_after_workplace(:p1)"),
                                       {"p1": workplace_id}).mappings().all()
        return [dict(row) for row in result]

    def get_workplace_after_router(self, router_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_workplace_after_router(:p1)"),
                                       {'p1': router_id}).mappings().all()
        return [dict(row) for row in result]