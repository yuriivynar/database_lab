from typing import List
from lab4.app.my_project.auth.dao import employee_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class EmployeeService(GeneralService):

    _dao = employee_dao

    def get_employee_after_position(self, position_id: int) -> List[object]:
        return self._dao.get_employee_after_position(position_id)