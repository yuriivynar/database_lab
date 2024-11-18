from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class AccessPointInWorkplace(db.Model, IDto):
    __tablename__ = "access_point_in_workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    access_point_id = db.Column(db.Integer, db.ForeignKey('access_point.id'), nullable=False)
    access_point = db.relationship("AccessPoint", backref="access_point_in_workplace")
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship("Workplace", backref="access_point_in_workplace")

    def __repr__(self) -> str:
        return f"AccessPointInWorkplace( '{self.access_point_id}', '{self.workplace_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "access_point_id": self.access_point_id,
            "workplace_id": self.workplace_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AccessPointInWorkplace:
        obj = AccessPointInWorkplace(**dto_dict)
        return obj