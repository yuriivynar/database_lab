from typing import List

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Brand
import sqlalchemy


class BrandDAO(GeneralDAO):
    _domain_type = Brand