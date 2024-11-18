from lab4.app.my_project.auth.dao import location_type_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class LocationTypeService(GeneralService):

    _dao = location_type_dao