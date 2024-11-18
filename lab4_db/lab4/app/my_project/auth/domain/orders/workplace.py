from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Workplace(db.Model, IDto):
    __tablename__ = "workplace"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    office_id = db.Column(db.Integer, db.ForeignKey('office.id'), nullable=False)
    office = db.relationship("Office", backref="workplace")
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship("Employee", backref="workplace")

    def __repr__(self) -> str:
        return f"Workplace({self.id}, '{self.office_id}', '{self.employee_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "office_id": self.office_id,
            "employee_id": self.employee_id,
            "name": self.employee.name,
            "surname": self.employee.surname,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Workplace:
        obj = Workplace(**dto_dict)
        return obj