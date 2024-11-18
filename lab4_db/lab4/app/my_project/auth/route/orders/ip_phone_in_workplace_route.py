from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import ip_phone_in_workplace_controller
from lab4.app.my_project.auth.domain import IpPhoneInWorkplace

ip_phone_in_workplace_bp = Blueprint('ip_phone_in_workplace', __name__, url_prefix='/ip_phone_in_workplace')


@ip_phone_in_workplace_bp.get('')
def get_all_ip_phone_in_workplaces() -> Response:
    return make_response(jsonify(ip_phone_in_workplace_controller.find_all()), HTTPStatus.OK)


@ip_phone_in_workplace_bp.post('')
def create_ip_phone_in_workplace() -> Response:
    content = request.get_json()
    ip_phone_in_workplace = IpPhoneInWorkplace.create_from_dto(content)
    ip_phone_in_workplace_controller.create(ip_phone_in_workplace)
    return make_response(jsonify(ip_phone_in_workplace.put_into_dto()), HTTPStatus.CREATED)


@ip_phone_in_workplace_bp.get('/<int:ip_phone_in_workplace_id>')
def get_ip_phone_in_workplace(ip_phone_in_workplace_id: int) -> Response:
    return make_response(jsonify(ip_phone_in_workplace_controller.find_by_id(ip_phone_in_workplace_id)), HTTPStatus.OK)


@ip_phone_in_workplace_bp.put('/<int:ip_phone_in_workplace_id>')
def update_ip_phone_in_workplace(ip_phone_in_workplace_id: int) -> Response:
    content = request.get_json()
    ip_phone_in_workplace = IpPhoneInWorkplace.create_from_dto(content)
    ip_phone_in_workplace_controller.update(ip_phone_in_workplace_id, ip_phone_in_workplace)
    return make_response("IpPhoneInWorkplace updated", HTTPStatus.OK)


@ip_phone_in_workplace_bp.patch('/<int:ip_phone_in_workplace_id>')
def patch_ip_phone_in_workplace(ip_phone_in_workplace_id: int) -> Response:
    content = request.get_json()
    ip_phone_in_workplace_controller.patch(ip_phone_in_workplace_id, content)
    return make_response("IpPhoneInWorkplace updated", HTTPStatus.OK)


@ip_phone_in_workplace_bp.delete('/<int:ip_phone_in_workplace_id>')
def delete_ip_phone_in_workplace(ip_phone_in_workplace_id: int) -> Response:
    ip_phone_in_workplace_controller.delete(ip_phone_in_workplace_id)
    return make_response("IpPhoneInWorkplace deleted", HTTPStatus.OK)

@ip_phone_in_workplace_bp.get('/get-ip-phone-after-workplace/<int:workplace_id>')
def get_ip_phone_after_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(ip_phone_in_workplace_controller.get_ip_phone_after_workplace(workplace_id)),
                         HTTPStatus.OK)

@ip_phone_in_workplace_bp.get('/get-workplace-after-ip-phone/<int:ip_phone_id>')
def get_workplace_after_ip_phone(ip_phone_id: int) -> Response:
    return make_response(jsonify(ip_phone_in_workplace_controller.get_workplace_after_ip_phone(ip_phone_id)),
                         HTTPStatus.OK)