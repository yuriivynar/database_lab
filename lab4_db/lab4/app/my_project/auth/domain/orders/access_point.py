from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class AccessPoint(db.Model, IDto):

    __tablename__ = "access_point"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    model = db.Column(db.String(45), nullable=False)
    ip_address = db.Column(db.String(20), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship("Brand", backref="access_point")

    def __repr__(self) -> str:
        return f"AccessPoint({self.id}, '{self.model}', '{self.ip_address}', '{self.brand_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "model": self.model,
            "ip_address": self.ip_address,
            "brand_id": self.brand_id,
            "brand_name": self.brand.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AccessPoint:
        obj = AccessPoint(**dto_dict)
        return obj