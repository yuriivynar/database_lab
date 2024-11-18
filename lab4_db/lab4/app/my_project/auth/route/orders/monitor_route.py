from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import monitor_controller
from lab4.app.my_project.auth.domain import Monitor

monitor_bp = Blueprint('monitors', __name__, url_prefix='/monitors')


@monitor_bp.get('')
def get_all_monitors() -> Response:
    return make_response(jsonify(monitor_controller.find_all()), HTTPStatus.OK)


@monitor_bp.post('')
def create_monitor() -> Response:
    content = request.get_json()
    monitor = Monitor.create_from_dto(content)
    monitor_controller.create(monitor)
    return make_response(jsonify(monitor.put_into_dto()), HTTPStatus.CREATED)


@monitor_bp.get('/<int:monitor_id>')
def get_monitor(monitor_id: int) -> Response:
    return make_response(jsonify(monitor_controller.find_by_id(monitor_id)), HTTPStatus.OK)


@monitor_bp.put('/<int:monitor_id>')
def update_monitor(monitor_id: int) -> Response:
    content = request.get_json()
    monitor = Monitor.create_from_dto(content)
    monitor_controller.update(monitor_id, monitor)
    return make_response("Monitor updated", HTTPStatus.OK)


@monitor_bp.patch('/<int:monitor_id>')
def patch_monitor(monitor_id: int) -> Response:
    content = request.get_json()
    monitor_controller.patch(monitor_id, content)
    return make_response("Monitor updated", HTTPStatus.OK)


@monitor_bp.delete('/<int:monitor_id>')
def delete_monitor(monitor_id: int) -> Response:
    monitor_controller.delete(monitor_id)
    return make_response("Monitor deleted", HTTPStatus.OK)

@monitor_bp.get('/get-monitor-after-brand-id/<int:brand_id>')
def get_monitor_after_brand_id(brand_id: int) -> Response:
    return make_response(jsonify(monitor_controller.get_monitor_after_brand_id(brand_id)),
                         HTTPStatus.OK)