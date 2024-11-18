from lab4.app.my_project.auth.dao import position_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class PositionService(GeneralService):

    _dao = position_dao