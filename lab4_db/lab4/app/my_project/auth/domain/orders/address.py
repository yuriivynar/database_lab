from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Address(db.Model, IDto):
    __tablename__ = "address"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    city = db.Column(db.String(25), nullable=False)
    street = db.Column(db.String(25), nullable=False)
    house_number = db.Column(db.String(25), nullable=False)
    office_number = db.Column(db.String(25), nullable=False)

    def __repr__(self) -> str:
        return f"Address({self.id}, '{self.city}', '{self.street}', '{self.house_number}', '{self.office_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "city": self.city,
            "street": self.street,
            "house_number": self.house_number,
            "office_number": self.office_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Address:
        obj = Address(**dto_dict)
        return obj
