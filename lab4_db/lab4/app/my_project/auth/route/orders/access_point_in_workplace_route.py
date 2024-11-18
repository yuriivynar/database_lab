from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import access_point_in_workplace_controller
from lab4.app.my_project.auth.domain import AccessPointInWorkplace

access_point_in_workplace_bp = Blueprint('access_point_in_workplace', __name__, url_prefix='/access_point_in_workplace')


@access_point_in_workplace_bp.get('')
def get_all_access_point_in_workplaces() -> Response:
    return make_response(jsonify(access_point_in_workplace_controller.find_all()), HTTPStatus.OK)


@access_point_in_workplace_bp.post('')
def create_access_point_in_workplace() -> Response:
    content = request.get_json()
    access_point_in_workplace = AccessPointInWorkplace.create_from_dto(content)
    access_point_in_workplace_controller.create(access_point_in_workplace)
    return make_response(jsonify(access_point_in_workplace.put_into_dto()), HTTPStatus.CREATED)


@access_point_in_workplace_bp.get('/<int:access_point_in_workplace_id>')
def get_access_point_in_workplace(access_point_in_workplace_id: int) -> Response:
    return make_response(jsonify(access_point_in_workplace_controller.find_by_id(access_point_in_workplace_id)), HTTPStatus.OK)


@access_point_in_workplace_bp.put('/<int:access_point_in_workplace_id>')
def update_access_point_in_workplace(access_point_in_workplace_id: int) -> Response:
    content = request.get_json()
    access_point_in_workplace = AccessPointInWorkplace.create_from_dto(content)
    access_point_in_workplace_controller.update(access_point_in_workplace_id, access_point_in_workplace)
    return make_response("Access_point_in_workplace updated", HTTPStatus.OK)


@access_point_in_workplace_bp.patch('/<int:access_point_in_workplace_id>')
def patch_access_point_in_workplace(access_point_in_workplace_id: int) -> Response:
    content = request.get_json()
    access_point_in_workplace_controller.patch(access_point_in_workplace_id, content)
    return make_response("Access_point_in_workplace updated", HTTPStatus.OK)


@access_point_in_workplace_bp.delete('/<int:access_point_in_workplace_id>')
def delete_access_point_in_workplace(access_point_in_workplace_id: int) -> Response:
    access_point_in_workplace_controller.delete(access_point_in_workplace_id)
    return make_response("Access_point_in_workplace deleted", HTTPStatus.OK)

@access_point_in_workplace_bp.get('/get-access-point-after-workplace/<int:workplace_id>')
def get_access_point_after_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(access_point_in_workplace_controller.get_access_point_after_workplace(workplace_id)),
                         HTTPStatus.OK)

@access_point_in_workplace_bp.get('/get-workplace-after-access-point/<int:access_point_id>')
def get_workplace_after_access_point(access_point_id: int) -> Response:
    return make_response(jsonify(access_point_in_workplace_controller.get_workplace_after_access_point(access_point_id)),
                         HTTPStatus.OK)