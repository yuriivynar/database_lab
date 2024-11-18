from typing import List

from lab4.app.my_project.auth.dao import computer_in_workplace_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ComputerInWorkplaceService(GeneralService):

    _dao = computer_in_workplace_dao

    def get_computer_after_workplace(self, workplace_id: int) -> List[object]:
        return self._dao.get_computer_after_workplace(workplace_id)

    def get_workplace_after_computer(self, computer_id: int) -> List[object]:
        return self._dao.get_workplace_after_computer(computer_id)