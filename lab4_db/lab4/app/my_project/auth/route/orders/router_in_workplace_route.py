from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import router_in_workplace_controller
from lab4.app.my_project.auth.domain import RouterInWorkplace

router_in_workplace_bp = Blueprint('router_in_workplace', __name__, url_prefix='/router_in_workplace')


@router_in_workplace_bp.get('')
def get_all_router_in_workplaces() -> Response:
    return make_response(jsonify(router_in_workplace_controller.find_all()), HTTPStatus.OK)


@router_in_workplace_bp.post('')
def create_router_in_workplace() -> Response:
    content = request.get_json()
    router_in_workplace = RouterInWorkplace.create_from_dto(content)
    router_in_workplace_controller.create(router_in_workplace)
    return make_response(jsonify(router_in_workplace.put_into_dto()), HTTPStatus.CREATED)


@router_in_workplace_bp.get('/<int:router_in_workplace_id>')
def get_router_in_workplace(router_in_workplace_id: int) -> Response:
    return make_response(jsonify(router_in_workplace_controller.find_by_id(router_in_workplace_id)), HTTPStatus.OK)


@router_in_workplace_bp.put('/<int:router_in_workplace_id>')
def update_router_in_workplace(router_in_workplace_id: int) -> Response:
    content = request.get_json()
    router_in_workplace = RouterInWorkplace.create_from_dto(content)
    router_in_workplace_controller.update(router_in_workplace_id, router_in_workplace)
    return make_response("RouterInWorkplace updated", HTTPStatus.OK)


@router_in_workplace_bp.patch('/<int:router_in_workplace_id>')
def patch_router_in_workplace(router_in_workplace_id: int) -> Response:
    content = request.get_json()
    router_in_workplace_controller.patch(router_in_workplace_id, content)
    return make_response("RouterInWorkplace updated", HTTPStatus.OK)


@router_in_workplace_bp.delete('/<int:router_in_workplace_id>')
def delete_router_in_workplace(router_in_workplace_id: int) -> Response:
    router_in_workplace_controller.delete(router_in_workplace_id)
    return make_response("RouterInWorkplace deleted", HTTPStatus.OK)

@router_in_workplace_bp.get('/get-router-after-workplace/<int:workplace_id>')
def get_router_after_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(router_in_workplace_controller.get_router_after_workplace(workplace_id)),
                         HTTPStatus.OK)

@router_in_workplace_bp.get('/get-workplace-after-router/<int:router_id>')
def get_workplace_after_router(router_id: int) -> Response:
    return make_response(jsonify(router_in_workplace_controller.get_workplace_after_router(router_id)),
                         HTTPStatus.OK)