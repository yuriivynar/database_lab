from lab4.app.my_project.auth.dao import type_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class TypeService(GeneralService):

    _dao = type_dao