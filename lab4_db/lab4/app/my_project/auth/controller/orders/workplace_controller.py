from typing import List
from lab4.app.my_project.auth.service import workplace_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class WorkplaceController(GeneralController):
    _service = workplace_service

    def get_employee_after_office(self, office_id: int) -> List[object]:
        return self._service.get_employee_after_office(office_id)

    def get_office_after_employee(self, employee_id: int) -> List[object]:
        return self._service.get_office_after_employee(employee_id)

