from lab4.app.my_project.auth.dao import address_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class AddressService(GeneralService):

    _dao = address_dao