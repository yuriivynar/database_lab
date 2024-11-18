from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Computer(db.Model, IDto):
    __tablename__ = "computer"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    cpu = db.Column(db.String(30), nullable=False)
    ram = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship("Brand", backref="computer")

    def __repr__(self) -> str:
        return f"Computer({self.id}, '{self.model}', '{self.cpu}', '{self.ram}', '{self.price}', '{self.brand_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "cpu": self.cpu,
            "ram": self.ram,
            "price": self.price,
            "brand_id": self.brand_id,
            "brand_name": self.brand.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Computer:
        obj = Computer(**dto_dict)
        return obj