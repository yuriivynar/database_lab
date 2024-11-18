from typing import List
from lab4.app.my_project.auth.dao import printer_in_workplace_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PrinterInWorkplaceService(GeneralService):

    _dao = printer_in_workplace_dao

    def get_printer_after_workplace(self, workplace_id: int) -> List[object]:
        return self._dao.get_printer_after_workplace(workplace_id)

    def get_workplace_after_printer(self, printer_id: int) -> List[object]:
        return self._dao.get_workplace_after_printer(printer_id)