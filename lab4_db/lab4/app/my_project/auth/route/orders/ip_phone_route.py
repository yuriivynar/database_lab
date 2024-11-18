from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import ip_phone_controller
from lab4.app.my_project.auth.domain import IpPhone

ip_phone_bp = Blueprint('ip_phones', __name__, url_prefix='/ip_phones')


@ip_phone_bp.get('')
def get_all_ip_phones() -> Response:
    return make_response(jsonify(ip_phone_controller.find_all()), HTTPStatus.OK)


@ip_phone_bp.post('')
def create_ip_phone() -> Response:
    content = request.get_json()
    ip_phone = IpPhone.create_from_dto(content)
    ip_phone_controller.create(ip_phone)
    return make_response(jsonify(ip_phone.put_into_dto()), HTTPStatus.CREATED)


@ip_phone_bp.get('/<int:ip_phone_id>')
def get_ip_phone(ip_phone_id: int) -> Response:
    return make_response(jsonify(ip_phone_controller.find_by_id(ip_phone_id)), HTTPStatus.OK)


@ip_phone_bp.put('/<int:ip_phone_id>')
def update_ip_phone(ip_phone_id: int) -> Response:
    content = request.get_json()
    ip_phone = IpPhone.create_from_dto(content)
    ip_phone_controller.update(ip_phone_id, ip_phone)
    return make_response("IpPhone updated", HTTPStatus.OK)


@ip_phone_bp.patch('/<int:ip_phone_id>')
def patch_ip_phone(ip_phone_id: int) -> Response:
    content = request.get_json()
    ip_phone_controller.patch(ip_phone_id, content)
    return make_response("IpPhone updated", HTTPStatus.OK)


@ip_phone_bp.delete('/<int:ip_phone_id>')
def delete_ip_phone(ip_phone_id: int) -> Response:
    ip_phone_controller.delete(ip_phone_id)
    return make_response("IpPhone deleted", HTTPStatus.OK)

@ip_phone_bp.get('/get-ip-phone-after-brand-id/<int:brand_id>')
def get_ip_phone_after_brand_id(brand_id: int) -> Response:
    return make_response(jsonify(ip_phone_controller.get_ip_phone_after_brand_id(brand_id)),
                         HTTPStatus.OK)