from typing import List
from lab4.app.my_project.auth.service import printer_in_workplace_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PrinterInWorkplaceController(GeneralController):
    _service = printer_in_workplace_service

    def get_printer_after_workplace(self, workplace_id: int) -> List[object]:
        return self._service.get_printer_after_workplace(workplace_id)

    def get_workplace_after_printer(self, printer_id: int) -> List[object]:
        return self._service.get_workplace_after_printer(printer_id)
