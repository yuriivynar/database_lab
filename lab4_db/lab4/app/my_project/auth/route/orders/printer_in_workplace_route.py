from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import printer_in_workplace_controller
from lab4.app.my_project.auth.domain import PrinterInWorkplace

printer_in_workplace_bp = Blueprint('printer_in_workplaces', __name__, url_prefix='/printer_in_workplaces')


@printer_in_workplace_bp.get('')
def get_all_printer_in_workplaces() -> Response:
    return make_response(jsonify(printer_in_workplace_controller.find_all()), HTTPStatus.OK)


@printer_in_workplace_bp.post('')
def create_printer_in_workplace() -> Response:
    content = request.get_json()
    printer_in_workplace = PrinterInWorkplace.create_from_dto(content)
    printer_in_workplace_controller.create(printer_in_workplace)
    return make_response(jsonify(printer_in_workplace.put_into_dto()), HTTPStatus.CREATED)


@printer_in_workplace_bp.get('/<int:printer_in_workplace_id>')
def get_printer_in_workplace(printer_in_workplace_id: int) -> Response:
    return make_response(jsonify(printer_in_workplace_controller.find_by_id(printer_in_workplace_id)), HTTPStatus.OK)


@printer_in_workplace_bp.put('/<int:printer_in_workplace_id>')
def update_printer_in_workplace(printer_in_workplace_id: int) -> Response:
    content = request.get_json()
    printer_in_workplace = PrinterInWorkplace.create_from_dto(content)
    printer_in_workplace_controller.update(printer_in_workplace_id, printer_in_workplace)
    return make_response("PrinterInWorkplace updated", HTTPStatus.OK)


@printer_in_workplace_bp.patch('/<int:printer_in_workplace_id>')
def patch_printer_in_workplace(printer_in_workplace_id: int) -> Response:
    content = request.get_json()
    printer_in_workplace_controller.patch(printer_in_workplace_id, content)
    return make_response("PrinterInWorkplace updated", HTTPStatus.OK)


@printer_in_workplace_bp.delete('/<int:printer_in_workplace_id>')
def delete_printer_in_workplace(printer_in_workplace_id: int) -> Response:
    printer_in_workplace_controller.delete(printer_in_workplace_id)
    return make_response("PrinterInWorkplace deleted", HTTPStatus.OK)

@printer_in_workplace_bp.get('/get-printer-after-workplace/<int:workplace_id>')
def get_printer_after_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(printer_in_workplace_controller.get_printer_after_workplace(workplace_id)),
                         HTTPStatus.OK)

@printer_in_workplace_bp.get('/get-workplace-after-printer/<int:printer_id>')
def get_workplace_after_printer(printer_id: int) -> Response:
    return make_response(jsonify(printer_in_workplace_controller.get_workplace_after_printer(printer_id)),
                         HTTPStatus.OK)