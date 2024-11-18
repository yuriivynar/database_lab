from typing import List, Dict, Any

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Office
import sqlalchemy


class OfficeDAO(GeneralDAO):
    _domain_type = Office

    def get_address_after_location_type(self, location_type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_address_after_location_type(:p1)"),
                                       {"p1": location_type_id}).mappings().all()
        return [dict(row) for row in result]

    def get_location_type_after_address(self, address_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_location_type_after_address(:p1)"),
                                       {'p1': address_id}).mappings().all()
        return [dict(row) for row in result]