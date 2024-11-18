from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class MonitorInWorkplace(db.Model, IDto):
    __tablename__ = "monitor_in_workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    monitor_id = db.Column(db.Integer, db.ForeignKey('monitor.id'), nullable=False)
    monitor = db.relationship("Monitor", backref="monitor_in_workplace")
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship("Workplace", backref="monitor_in_workplace")

    def __repr__(self) -> str:
        return f"MonitorInWorkplace( '{self.monitor_id}', '{self.workplace_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "monitor_id": self.monitor_id,
            "workplace_id": self.workplace_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MonitorInWorkplace:
        obj = MonitorInWorkplace(**dto_dict)
        return obj