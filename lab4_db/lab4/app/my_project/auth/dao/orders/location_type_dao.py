from typing import List

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import LocationType
import sqlalchemy


class LocationTypeDAO(GeneralDAO):
    _domain_type = LocationType