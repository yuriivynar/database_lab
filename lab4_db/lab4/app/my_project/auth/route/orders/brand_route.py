from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import brand_controller
from lab4.app.my_project.auth.domain import Brand

brand_bp = Blueprint('brand', __name__, url_prefix='/brand')


@brand_bp.get('')
def get_all_brands() -> Response:
    return make_response(jsonify(brand_controller.find_all()), HTTPStatus.OK)


@brand_bp.post('')
def create_brand() -> Response:
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.create(brand)
    return make_response(jsonify(brand.put_into_dto()), HTTPStatus.CREATED)


@brand_bp.get('/<int:brand_id>')
def get_brand(brand_id: int) -> Response:
    return make_response(jsonify(brand_controller.find_by_id(brand_id)), HTTPStatus.OK)


@brand_bp.put('/<int:brand_id>')
def update_brand(brand_id: int) -> Response:
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.update(brand_id, brand)
    return make_response("Brand updated", HTTPStatus.OK)


@brand_bp.patch('/<int:brand_id>')
def patch_brand(brand_id: int) -> Response:
    content = request.get_json()
    brand_controller.patch(brand_id, content)
    return make_response("Brand updated", HTTPStatus.OK)


@brand_bp.delete('/<int:brand_id>')
def delete_brand(brand_id: int) -> Response:
    brand_controller.delete(brand_id)
    return make_response("Brand deleted", HTTPStatus.OK)