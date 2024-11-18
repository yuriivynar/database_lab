from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Monitor(db.Model, IDto):
    __tablename__ = "monitor"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    resolution = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship("Brand", backref="monitor")

    def __repr__(self) -> str:
        return f"Monitor({self.id}, '{self.model}', '{self.resolution}', '{self.price}', '{self.brand_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "resolution": self.resolution,
            "price": self.price,
            "brand_id": self.brand_id,
            "brand_name": self.brand.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Monitor:
        obj = Monitor(**dto_dict)
        return obj