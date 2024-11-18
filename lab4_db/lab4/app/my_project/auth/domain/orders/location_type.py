from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class LocationType(db.Model, IDto):
    __tablename__ = "location_type"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    location_name = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"LocationType({self.id}, '{self.location_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "location_name": self.location_name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> LocationType:
        obj = LocationType(**dto_dict)
        return obj