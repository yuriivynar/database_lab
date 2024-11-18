from typing import List, Dict, Any
from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import IpPhoneInWorkplace
import sqlalchemy


class IpPhoneInWorkplaceDAO(GeneralDAO):
    _domain_type = IpPhoneInWorkplace

    def get_ip_phone_after_workplace(self, workplace_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_ip_phone_after_workplace(:p1)"),
                                       {"p1": workplace_id}).mappings().all()
        return [dict(row) for row in result]

    def get_workplace_after_ip_phone(self, ip_phone_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_workplace_after_ip_phone(:p1)"),
                                       {'p1': ip_phone_id}).mappings().all()
        return [dict(row) for row in result]