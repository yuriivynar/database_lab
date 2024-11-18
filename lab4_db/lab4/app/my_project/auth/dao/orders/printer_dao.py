from typing import List, Dict, Any

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Printer
import sqlalchemy


class PrinterDAO(GeneralDAO):
    _domain_type = Printer

    def get_printer_after_type(self, type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_printer_after_type(:p1)"),
                                       {'p1': type_id}).mappings().all()
        return [dict(row) for row in result]

    def get_printer_after_brand_id(self, brand_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_printer_after_brand_id(:p1)"),
                                       {"p1": brand_id}).mappings().all()
        return [dict(row) for row in result]
