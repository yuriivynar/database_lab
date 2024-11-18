from lab4.app.my_project.auth.dao import brand_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class BrandService(GeneralService):

    _dao = brand_dao