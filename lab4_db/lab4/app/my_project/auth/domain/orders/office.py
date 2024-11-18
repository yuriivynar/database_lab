from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Office(db.Model, IDto):
    __tablename__ = "office"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    address = db.relationship("Address", backref="office")
    location_type_id = db.Column(db.Integer, db.ForeignKey('location_type.id'), nullable=False)
    location_type = db.relationship("LocationType", backref="office")

    def __repr__(self) -> str:
        return f"Office({self.id}, '{self.address_id}', '{self.location_type_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "address_id": self.address_id,
            "address_city": self.address.city,
            "address_street": self.address.street,
            "location_type": self.location_type.location_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Office:
        obj = Office(**dto_dict)
        return obj