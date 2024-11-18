from typing import List, Dict, Any
from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import PrinterInWorkplace
import sqlalchemy


class PrinterInWorkplaceDAO(GeneralDAO):
    _domain_type = PrinterInWorkplace

    def get_printer_after_workplace(self, workplace_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_printer_after_workplace(:p1)"),
                                       {"p1": workplace_id}).mappings().all()
        return [dict(row) for row in result]

    def get_workplace_after_printer(self, printer_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_workplace_after_printer(:p1)"),
                                       {'p1': printer_id}).mappings().all()
        return [dict(row) for row in result]