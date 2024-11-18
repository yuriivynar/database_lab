from typing import List

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Position
import sqlalchemy


class PositionDAO(GeneralDAO):
    _domain_type = Position