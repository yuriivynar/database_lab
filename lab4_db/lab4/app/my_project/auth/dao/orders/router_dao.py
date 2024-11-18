from typing import List, Dict, Any

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Router
import sqlalchemy


class RouterDAO(GeneralDAO):
    _domain_type = Router

    def get_router_after_brand_id(self, brand_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_router_after_brand_id(:p1)"),
                                       {"p1": brand_id}).mappings().all()
        return [dict(row) for row in result]