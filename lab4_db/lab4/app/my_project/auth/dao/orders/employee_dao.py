from typing import List, Dict, Any

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Employee
import sqlalchemy


class EmployeeDAO(GeneralDAO):
    _domain_type = Employee

    def get_employee_after_position(self, position_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_employee_after_position(:p1)"),
                                       {"p1": position_id}).mappings().all()
        return [dict(row) for row in result]