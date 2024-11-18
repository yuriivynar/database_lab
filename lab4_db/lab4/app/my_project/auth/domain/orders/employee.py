from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Employee(db.Model, IDto):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    pass_number = db.Column(db.String(20), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)
    position = db.relationship("Position", backref="employees")

    def __repr__(self) -> str:
        return f"Employee({self.id}, '{self.name}', '{self.surname}', '{self.pass_number}', '{self.position_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "pass_number": self.pass_number,
            "position_name": self.position.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        obj = Employee(**dto_dict)
        return obj
