from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class IpPhoneInWorkplace(db.Model, IDto):
    __tablename__ = "ip_phone_in_workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    ip_phone_id = db.Column(db.Integer, db.ForeignKey('ip_phone.id'), nullable=False)
    ip_phone = db.relationship("IpPhone", backref="ip_phone_in_workplace")
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = db.relationship("Workplace", backref="ip_phone_in_workplace")

    def __repr__(self) -> str:
        return f"IpPhoneInWorkplace( '{self.ip_phone_id}', '{self.workplace_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "ip_phone_id": self.ip_phone_id,
            "workplace_id": self.workplace_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> IpPhoneInWorkplace:
        obj = IpPhoneInWorkplace(**dto_dict)
        return obj