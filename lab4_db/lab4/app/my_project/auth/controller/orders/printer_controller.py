from typing import List
from lab4.app.my_project.auth.service import printer_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class PrinterController(GeneralController):
    _service = printer_service

    def get_printer_after_type(self, type_id: int) -> List[object]:
        return self._service.get_printer_after_type(type_id)

    def get_printer_after_brand_id(self, brand_id: int) -> List[object]:
        return self._service.get_printer_after_brand_id(brand_id)