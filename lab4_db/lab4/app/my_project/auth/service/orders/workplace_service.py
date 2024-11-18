from typing import List
from lab4.app.my_project.auth.dao import workplace_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WorkplaceService(GeneralService):

    _dao = workplace_dao

    def get_employee_after_office(self, office_id: int) -> List[object]:
        return self._dao.get_employee_after_office(office_id)

    def get_office_after_employee(self, employee_id: int) -> List[object]:
        return self._dao.get_office_after_employee(employee_id)