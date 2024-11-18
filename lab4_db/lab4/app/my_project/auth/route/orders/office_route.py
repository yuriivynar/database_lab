from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import office_controller
from lab4.app.my_project.auth.domain import Office

office_bp = Blueprint('offices', __name__, url_prefix='/offices')


@office_bp.get('')
def get_all_offices() -> Response:
    return make_response(jsonify(office_controller.find_all()), HTTPStatus.OK)


@office_bp.post('')
def create_office() -> Response:
    content = request.get_json()
    office = Office.create_from_dto(content)
    office_controller.create(office)
    return make_response(jsonify(office.put_into_dto()), HTTPStatus.CREATED)


@office_bp.get('/<int:office_id>')
def get_office(office_id: int) -> Response:
    return make_response(jsonify(office_controller.find_by_id(office_id)), HTTPStatus.OK)


@office_bp.put('/<int:office_id>')
def update_office(office_id: int) -> Response:
    content = request.get_json()
    office = Office.create_from_dto(content)
    office_controller.update(office_id, office)
    return make_response("Office updated", HTTPStatus.OK)


@office_bp.patch('/<int:office_id>')
def patch_office(office_id: int) -> Response:
    content = request.get_json()
    office_controller.patch(office_id, content)
    return make_response("Office updated", HTTPStatus.OK)


@office_bp.delete('/<int:office_id>')
def delete_office(office_id: int) -> Response:
    office_controller.delete(office_id)
    return make_response("Office deleted", HTTPStatus.OK)

@office_bp.get('/get-address-after-location-type/<int:location_type_id>')
def get_address_after_location_type(location_type_id: int) -> Response:
    return make_response(jsonify(office_controller.get_address_after_location_type(location_type_id)),
                         HTTPStatus.OK)

@office_bp.get('/get-location-type-after-address/<int:address_id>')
def get_location_type_after_address(address_id: int) -> Response:
    return make_response(jsonify(office_controller.get_location_type_after_address(address_id)),
                         HTTPStatus.OK)