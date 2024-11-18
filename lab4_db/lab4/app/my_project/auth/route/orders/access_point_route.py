from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import access_point_controller
from lab4.app.my_project.auth.domain import AccessPoint

access_point_bp = Blueprint('access_points', __name__, url_prefix='/access_points')


@access_point_bp.get('')
def get_all_access_points() -> Response:
    return make_response(jsonify(access_point_controller.find_all()), HTTPStatus.OK)


@access_point_bp.post('')
def create_access_point() -> Response:
    content = request.get_json()
    access_point = AccessPoint.create_from_dto(content)
    access_point_controller.create(access_point)
    return make_response(jsonify(access_point.put_into_dto()), HTTPStatus.CREATED)


@access_point_bp.get('/<int:access_point_id>')
def get_access_point(access_point_id: int) -> Response:
    return make_response(jsonify(access_point_controller.find_by_id(access_point_id)), HTTPStatus.OK)


@access_point_bp.put('/<int:access_point_id>')
def update_access_point(access_point_id: int) -> Response:
    content = request.get_json()
    access_point = AccessPoint.create_from_dto(content)
    access_point_controller.update(access_point_id, access_point)
    return make_response("Access_point updated", HTTPStatus.OK)


@access_point_bp.patch('/<int:access_point_id>')
def patch_access_point(access_point_id: int) -> Response:
    content = request.get_json()
    access_point_controller.patch(access_point_id, content)
    return make_response("Access_point updated", HTTPStatus.OK)


@access_point_bp.delete('/<int:access_point_id>')
def delete_access_point(access_point_id: int) -> Response:
    access_point_controller.delete(access_point_id)
    return make_response("Access_point deleted", HTTPStatus.OK)

@access_point_bp.get('/get-access-point-after-brand-id/<int:brand_id>')
def get_access_point_after_brand_id(brand_id: int) -> Response:
    return make_response(jsonify(access_point_controller.get_access_point_after_brand_id(brand_id)),
                         HTTPStatus.OK)
