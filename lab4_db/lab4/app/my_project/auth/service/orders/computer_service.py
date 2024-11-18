from typing import List
from lab4.app.my_project.auth.dao import computer_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class ComputerService(GeneralService):

    _dao = computer_dao

    def get_computer_after_brand_id(self, brand_id: int) -> List[object]:
        return self._dao.get_computer_after_brand_id(brand_id)