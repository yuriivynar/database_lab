from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class ComputerInWorkplace(db.Model, IDto):
    __tablename__ = "computer_in_workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    computer_id = db.Column(db.Integer, db.ForeignKey('computer.id'), nullable=False)
    computer = db.relationship("Computer", backref="computer_in_workplace")
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship("Workplace", backref="computer_in_workplace")

    def __repr__(self) -> str:
        return f"ComputerInWorkplace( '{self.computer_id}', '{self.workplace_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "computer_id": self.computer_id,
            "workplace_id": self.workplace_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ComputerInWorkplace:
        obj = ComputerInWorkplace(**dto_dict)
        return obj