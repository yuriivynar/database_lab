from typing import List
from lab4.app.my_project.auth.service import computer_in_workplace_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class ComputerInWorkplaceController(GeneralController):
    _service = computer_in_workplace_service

    def get_computer_after_workplace(self, workplace_id: int) -> List[object]:
        return self._service.get_computer_after_workplace(workplace_id)

    def get_workplace_after_computer(self, computer_id: int) -> List[object]:
        return self._service.get_workplace_after_computer(computer_id)

