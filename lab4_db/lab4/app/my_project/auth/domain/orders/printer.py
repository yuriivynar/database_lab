from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Printer(db.Model, IDto):
    __tablename__ = "printer"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    type = db.relationship("Type", backref="printer")
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship("Brand", backref="printer")

    def __repr__(self) -> str:
        return f"Printer({self.id}, '{self.model}', '{self.price}', '{self.brand_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "price": self.price,
            "brand_id": self.brand_id,
            "brand_name": self.brand.name,
            "type_id": self.type,
            "type": self.type.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Printer:
        obj = Printer(**dto_dict)
        return obj