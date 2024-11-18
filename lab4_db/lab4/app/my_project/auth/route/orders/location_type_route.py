from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import location_type_controller
from lab4.app.my_project.auth.domain import LocationType

location_type_bp = Blueprint('location_types', __name__, url_prefix='/location_types')


@location_type_bp.get('')
def get_all_location_types() -> Response:
    return make_response(jsonify(location_type_controller.find_all()), HTTPStatus.OK)


@location_type_bp.post('')
def create_location_type() -> Response:
    content = request.get_json()
    location_type = LocationType.create_from_dto(content)
    location_type_controller.create(location_type)
    return make_response(jsonify(location_type.put_into_dto()), HTTPStatus.CREATED)


@location_type_bp.get('/<int:location_type_id>')
def get_location_type(location_type_id: int) -> Response:
    return make_response(jsonify(location_type_controller.find_by_id(location_type_id)), HTTPStatus.OK)


@location_type_bp.put('/<int:location_type_id>')
def update_location_type(location_type_id: int) -> Response:
    content = request.get_json()
    location_type = LocationType.create_from_dto(content)
    location_type_controller.update(location_type_id, location_type)
    return make_response("LocationType updated", HTTPStatus.OK)


@location_type_bp.patch('/<int:location_type_id>')
def patch_location_type(location_type_id: int) -> Response:
    content = request.get_json()
    location_type_controller.patch(location_type_id, content)
    return make_response("LocationType updated", HTTPStatus.OK)


@location_type_bp.delete('/<int:location_type_id>')
def delete_location_type(location_type_id: int) -> Response:
    location_type_controller.delete(location_type_id)
    return make_response("Access_point deleted", HTTPStatus.OK)