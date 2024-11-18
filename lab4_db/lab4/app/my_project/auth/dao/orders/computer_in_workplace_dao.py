from typing import List, Dict, Any

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import ComputerInWorkplace
import sqlalchemy


class ComputerInWorkplaceDAO(GeneralDAO):
    _domain_type = ComputerInWorkplace

    def get_computer_after_workplace(self, workplace_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_computer_after_workplace(:p1)"),
                                       {"p1": workplace_id}).mappings().all()
        return [dict(row) for row in result]

    def get_workplace_after_computer(self, computer_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_workplace_after_computer(:p1)"),
                                       {'p1': computer_id}).mappings().all()
        return [dict(row) for row in result]