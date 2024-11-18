from typing import List

from lab4.app.my_project.auth.service import employee_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class EmployeeController(GeneralController):
    _service = employee_service

    def get_employee_after_position(self, position_id: int) -> List[object]:
        return self._service.get_employee_after_position(position_id)

