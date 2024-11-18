from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import printer_controller
from lab4.app.my_project.auth.domain import Printer

printer_bp = Blueprint('printers', __name__, url_prefix='/printers')


@printer_bp.get('')
def get_all_printers() -> Response:
    return make_response(jsonify(printer_controller.find_all()), HTTPStatus.OK)


@printer_bp.post('')
def create_printer() -> Response:
    content = request.get_json()
    printer = Printer.create_from_dto(content)
    printer_controller.create(printer)
    return make_response(jsonify(printer.put_into_dto()), HTTPStatus.CREATED)


@printer_bp.get('/<int:printer_id>')
def get_printer(printer_id: int) -> Response:
    return make_response(jsonify(printer_controller.find_by_id(printer_id)), HTTPStatus.OK)


@printer_bp.put('/<int:printer_id>')
def update_printer(printer_id: int) -> Response:
    content = request.get_json()
    printer = Printer.create_from_dto(content)
    printer_controller.update(printer_id, printer)
    return make_response("Printer updated", HTTPStatus.OK)


@printer_bp.patch('/<int:printer_id>')
def patch_printer(printer_id: int) -> Response:
    content = request.get_json()
    printer_controller.patch(printer_id, content)
    return make_response("Printer updated", HTTPStatus.OK)


@printer_bp.delete('/<int:printer_id>')
def delete_printer(printer_id: int) -> Response:
    printer_controller.delete(printer_id)
    return make_response("Printer deleted", HTTPStatus.OK)

@printer_bp.get('/get-printer-after-type/<int:type_id>')
def get_printer_after_type(type_id: int) -> Response:
    return make_response(jsonify(printer_controller.get_printer_after_type(type_id)),
                         HTTPStatus.OK)
@printer_bp.get('/get-printer-after-brand-id/<int:brand_id>')
def get_printer_after_brand_id(brand_id: int) -> Response:
    return make_response(jsonify(printer_controller.get_printer_after_brand_id(brand_id)),
                         HTTPStatus.OK)