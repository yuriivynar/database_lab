from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import monitor_in_workplace_controller
from lab4.app.my_project.auth.domain import MonitorInWorkplace

monitor_in_workplace_bp = Blueprint('monitor_in_workplace', __name__, url_prefix='/monitor_in_workplace')


@monitor_in_workplace_bp.get('')
def get_all_access_points() -> Response:
    return make_response(jsonify(monitor_in_workplace_controller.find_all()), HTTPStatus.OK)


@monitor_in_workplace_bp.post('')
def create_access_point() -> Response:
    content = request.get_json()
    monitor_in_workplace = MonitorInWorkplace.create_from_dto(content)
    monitor_in_workplace_controller.create(monitor_in_workplace)
    return make_response(jsonify(monitor_in_workplace.put_into_dto()), HTTPStatus.CREATED)


@monitor_in_workplace_bp.get('/<int:monitor_in_workplace_id>')
def get_access_point(monitor_in_workplace_id: int) -> Response:
    return make_response(jsonify(monitor_in_workplace_controller.find_by_id(monitor_in_workplace_id)), HTTPStatus.OK)


@monitor_in_workplace_bp.put('/<int:monitor_in_workplace_id>')
def update_access_point(monitor_in_workplace_id: int) -> Response:
    content = request.get_json()
    monitor_in_workplace = MonitorInWorkplace.create_from_dto(content)
    monitor_in_workplace_controller.update(monitor_in_workplace_id, monitor_in_workplace)
    return make_response("MonitorInWorkplace updated", HTTPStatus.OK)


@monitor_in_workplace_bp.patch('/<int:monitor_in_workplace_id>')
def patch_access_point(monitor_in_workplace_id: int) -> Response:
    content = request.get_json()
    monitor_in_workplace_controller.patch(monitor_in_workplace_id, content)
    return make_response("MonitorInWorkplace updated", HTTPStatus.OK)


@monitor_in_workplace_bp.delete('/<int:monitor_in_workplace_id>')
def delete_access_point(monitor_in_workplace_id: int) -> Response:
    monitor_in_workplace_controller.delete(monitor_in_workplace_id)
    return make_response("MonitorInWorkplace deleted", HTTPStatus.OK)

@monitor_in_workplace_bp.get('/get-monitor-after-workplace/<int:workplace_id>')
def get_monitor_after_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(monitor_in_workplace_controller.get_monitor_after_workplace(workplace_id)),
                         HTTPStatus.OK)

@monitor_in_workplace_bp.get('/get-workplace-after-monitor/<int:monitor_id>')
def get_workplace_after_monitor(monitor_id: int) -> Response:
    return make_response(jsonify(monitor_in_workplace_controller.get_workplace_after_monitor(monitor_id)),
                         HTTPStatus.OK)