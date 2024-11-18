from typing import List
from lab4.app.my_project.auth.dao import printer_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PrinterService(GeneralService):

    _dao = printer_dao

    def get_printer_after_type(self, type_id: int) -> List[object]:
        return self._dao.get_printer_after_type(type_id)

    def get_printer_after_brand_id(self, brand_id: int) -> List[object]:
        return self._dao.get_printer_after_brand_id(brand_id)