from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import computer_controller
from lab4.app.my_project.auth.domain import Computer

computer_bp = Blueprint('computers', __name__, url_prefix='/computers')


@computer_bp.get('')
def get_all_computers() -> Response:
    return make_response(jsonify(computer_controller.find_all()), HTTPStatus.OK)


@computer_bp.post('')
def create_computer() -> Response:
    content = request.get_json()
    computer = Computer.create_from_dto(content)
    computer_controller.create(computer)
    return make_response(jsonify(computer.put_into_dto()), HTTPStatus.CREATED)


@computer_bp.get('/<int:computer_id>')
def get_access_point(computer_id: int) -> Response:
    return make_response(jsonify(computer_controller.find_by_id(computer_id)), HTTPStatus.OK)


@computer_bp.put('/<int:computer_id>')
def update_access_point(computer_id: int) -> Response:
    content = request.get_json()
    computer = Computer.create_from_dto(content)
    computer_controller.update(computer_id, computer)
    return make_response("Computer updated", HTTPStatus.OK)


@computer_bp.patch('/<int:computer_id>')
def patch_access_point(computer_id: int) -> Response:
    content = request.get_json()
    computer_controller.patch(computer_id, content)
    return make_response("Computer updated", HTTPStatus.OK)


@computer_bp.delete('/<int:computer_id>')
def delete_access_point(computer_id: int) -> Response:
    computer_controller.delete(computer_id)
    return make_response("Computer deleted", HTTPStatus.OK)

@computer_bp.get('/get-computer-after-brand-id/<int:brand_id>')
def get_computer_after_brand_id(brand_id: int) -> Response:
    return make_response(jsonify(computer_controller.get_computer_after_brand_id(brand_id)),
                         HTTPStatus.OK)