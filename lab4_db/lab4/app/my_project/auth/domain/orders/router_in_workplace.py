from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class RouterInWorkplace(db.Model, IDto):
    __tablename__ = "router_in_workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    router_id = db.Column(db.Integer, db.ForeignKey('router.id'), nullable=False)
    router = db.relationship("Router", backref="router_in_workplace")
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship("Workplace", backref="router_in_workplace")

    def __repr__(self) -> str:
        return f"RouterInWorkplace( '{self.router_id}', '{self.workplace_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "router_id": self.router_id,
            "workplace_id": self.workplace_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RouterInWorkplace:
        obj = RouterInWorkplace(**dto_dict)
        return obj