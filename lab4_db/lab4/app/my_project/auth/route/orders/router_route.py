from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import router_controller
from lab4.app.my_project.auth.domain import Router

router_bp = Blueprint('routers', __name__, url_prefix='/routers')


@router_bp.get('')
def get_all_routers() -> Response:
    return make_response(jsonify(router_controller.find_all()), HTTPStatus.OK)


@router_bp.post('')
def create_router() -> Response:
    content = request.get_json()
    router = Router.create_from_dto(content)
    router_controller.create(router)
    return make_response(jsonify(router.put_into_dto()), HTTPStatus.CREATED)


@router_bp.get('/<int:router_id>')
def get_router(router_id: int) -> Response:
    return make_response(jsonify(router_controller.find_by_id(router_id)), HTTPStatus.OK)


@router_bp.put('/<int:router_id>')
def update_router(router_id: int) -> Response:
    content = request.get_json()
    router = Router.create_from_dto(content)
    router_controller.update(router_id, router)
    return make_response("Router updated", HTTPStatus.OK)


@router_bp.patch('/<int:router_id>')
def patch_router(router_id: int) -> Response:
    content = request.get_json()
    router_controller.patch(router_id, content)
    return make_response("Router updated", HTTPStatus.OK)


@router_bp.delete('/<int:router_id>')
def delete_router(router_id: int) -> Response:
    router_controller.delete(router_id)
    return make_response("Router deleted", HTTPStatus.OK)

@router_bp.get('/get-router-after-brand-id/<int:brand_id>')
def get_router_after_brand_id(brand_id: int) -> Response:
    return make_response(jsonify(router_controller.get_router_after_brand_id(brand_id)),
                         HTTPStatus.OK)