from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import position_controller
from lab4.app.my_project.auth.domain import Position

position_bp = Blueprint('positions', __name__, url_prefix='/positions')


@position_bp.get('')
def get_all_positions() -> Response:
    return make_response(jsonify(position_controller.find_all()), HTTPStatus.OK)


@position_bp.post('')
def create_position() -> Response:
    content = request.get_json()
    position = Position.create_from_dto(content)
    position_controller.create(position)
    return make_response(jsonify(position.put_into_dto()), HTTPStatus.CREATED)


@position_bp.get('/<int:position_id>')
def get_position(position_id: int) -> Response:
    return make_response(jsonify(position_controller.find_by_id(position_id)), HTTPStatus.OK)


@position_bp.put('/<int:position_id>')
def update_position(position_id: int) -> Response:
    content = request.get_json()
    position = Position.create_from_dto(content)
    position_controller.update(position_id, position)
    return make_response("Position updated", HTTPStatus.OK)


@position_bp.patch('/<int:position_id>')
def patch_position(position_id: int) -> Response:
    content = request.get_json()
    position_controller.patch(position_id, content)
    return make_response("Position updated", HTTPStatus.OK)


@position_bp.delete('/<int:position_id>')
def delete_position(position_id: int) -> Response:
    position_controller.delete(position_id)
    return make_response("Position deleted", HTTPStatus.OK)