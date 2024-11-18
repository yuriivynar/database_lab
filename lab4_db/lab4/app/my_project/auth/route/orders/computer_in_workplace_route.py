from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import computer_in_workplace_controller
from lab4.app.my_project.auth.domain import ComputerInWorkplace

computer_in_workplace_bp = Blueprint('computer_in_workplace', __name__, url_prefix='/computer_in_workplace')


@computer_in_workplace_bp.get('')
def get_all_computer_in_workplaces() -> Response:
    return make_response(jsonify(computer_in_workplace_controller.find_all()), HTTPStatus.OK)


@computer_in_workplace_bp.post('')
def create_computer_in_workplace() -> Response:
    content = request.get_json()
    computer_in_workplace = ComputerInWorkplace.create_from_dto(content)
    computer_in_workplace_controller.create(computer_in_workplace)
    return make_response(jsonify(computer_in_workplace.put_into_dto()), HTTPStatus.CREATED)


@computer_in_workplace_bp.get('/<int:computer_in_workplace_id>')
def get_computer_in_workplace(computer_in_workplace_id: int) -> Response:
    return make_response(jsonify(computer_in_workplace_controller.find_by_id(computer_in_workplace_id)), HTTPStatus.OK)


@computer_in_workplace_bp.put('/<int:computer_in_workplace_id>')
def update_computer_in_workplace(computer_in_workplace_id: int) -> Response:
    content = request.get_json()
    computer_in_workplace = ComputerInWorkplace.create_from_dto(content)
    computer_in_workplace_controller.update(computer_in_workplace_id, computer_in_workplace)
    return make_response("ComputerInWorkplace updated", HTTPStatus.OK)


@computer_in_workplace_bp.patch('/<int:computer_in_workplace_id>')
def patch_access_point(computer_in_workplace_id: int) -> Response:
    content = request.get_json()
    computer_in_workplace_controller.patch(computer_in_workplace_id, content)
    return make_response("ComputerInWorkplace updated", HTTPStatus.OK)


@computer_in_workplace_bp.delete('/<int:computer_in_workplace_id>')
def delete_access_point(computer_in_workplace_id: int) -> Response:
    computer_in_workplace_controller.delete(computer_in_workplace_id)
    return make_response("ComputerInWorkplace deleted", HTTPStatus.OK)

@computer_in_workplace_bp.get('/get-computer-after-workplace/<int:workplace_id>')
def get_computer_after_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(computer_in_workplace_controller.get_computer_after_workplace(workplace_id)),
                         HTTPStatus.OK)

@computer_in_workplace_bp.get('/get-workplace-after-computer/<int:computer_id>')
def get_workplace_after_computer(computer_id: int) -> Response:
    return make_response(jsonify(computer_in_workplace_controller.get_workplace_after_computer(computer_id)),
                         HTTPStatus.OK)