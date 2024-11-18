from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class PrinterInWorkplace(db.Model, IDto):
    __tablename__ = "printer_in_workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    printer_id = db.Column(db.Integer, db.ForeignKey('printer.id'), nullable=False)
    printer = db.relationship("Printer", backref="printer_in_workplace")
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship("Workplace", backref="printer_in_workplace")

    def __repr__(self) -> str:
        return f"PrinterInWorkplace( '{self.printer_id}', '{self.workplace_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "printer_id": self.printer_id,
            "workplace_id": self.workplace_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PrinterInWorkplace:
        obj = PrinterInWorkplace(**dto_dict)
        return obj