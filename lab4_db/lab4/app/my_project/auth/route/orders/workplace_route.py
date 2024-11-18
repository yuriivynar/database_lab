from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import workplace_controller
from lab4.app.my_project.auth.domain import Workplace

workplace_bp = Blueprint('workplaces', __name__, url_prefix='/workplaces')


@workplace_bp.get('')
def get_all_workplaces() -> Response:
    return make_response(jsonify(workplace_controller.find_all()), HTTPStatus.OK)


@workplace_bp.post('')
def create_workplace() -> Response:
    content = request.get_json()
    workplace = Workplace.create_from_dto(content)
    workplace_controller.create(workplace)
    return make_response(jsonify(workplace.put_into_dto()), HTTPStatus.CREATED)


@workplace_bp.get('/<int:workplace_id>')
def get_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(workplace_controller.find_by_id(workplace_id)), HTTPStatus.OK)


@workplace_bp.put('/<int:workplace_id>')
def update_workplace(workplace_id: int) -> Response:
    content = request.get_json()
    workplace = Workplace.create_from_dto(content)
    workplace_controller.update(workplace_id, workplace)
    return make_response("Workplace updated", HTTPStatus.OK)


@workplace_bp.patch('/<int:workplace_id>')
def patch_workplace(workplace_id: int) -> Response:
    content = request.get_json()
    workplace_controller.patch(workplace_id, content)
    return make_response("Workplace updated", HTTPStatus.OK)


@workplace_bp.delete('/<int:workplace_id>')
def delete_workplace(workplace_id: int) -> Response:
    workplace_controller.delete(workplace_id)
    return make_response("Workplace deleted", HTTPStatus.OK)

@workplace_bp.get('/get-employee-after-office/<int:office_id>')
def get_employee_after_office(office_id: int) -> Response:
    return make_response(jsonify(workplace_controller.get_employee_after_office(office_id)),
                         HTTPStatus.OK)

@workplace_bp.get('/get-office-after-employee/<int:employee_id>')
def get_office_after_employee(employee_id: int) -> Response:
    return make_response(jsonify(workplace_controller.get_office_after_employee(employee_id)),
                         HTTPStatus.OK)