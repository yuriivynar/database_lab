from flask import Flask
from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .orders.access_point_route import access_point_bp
    from .orders.access_point_in_workplace_route import access_point_in_workplace_bp
    from .orders.address_route import address_bp
    from .orders.brand_route import brand_bp
    from .orders.computer_in_workplace_route import computer_in_workplace_bp
    from .orders.computer_route import computer_bp
    from .orders.employee_route import employee_bp
    from .orders.ip_phone_in_workplace_route import ip_phone_in_workplace_bp
    from .orders.ip_phone_route import ip_phone_bp
    from .orders.location_type_route import location_type_bp
    from .orders.monitor_in_workplace_route import monitor_in_workplace_bp
    from .orders.monitor_route import monitor_bp
    from .orders.office_route import office_bp
    from .orders.position_route import position_bp
    from .orders.printer_in_workplace_route import printer_in_workplace_bp
    from .orders.printer_route import printer_bp
    from .orders.router_in_workplace_route import router_in_workplace_bp
    from .orders.router_route import router_bp
    from .orders.type_route import type_bp
    from .orders.workplace_route import workplace_bp


    app.register_blueprint(access_point_bp)
    app.register_blueprint(access_point_in_workplace_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(computer_in_workplace_bp)
    app.register_blueprint(computer_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(ip_phone_in_workplace_bp)
    app.register_blueprint(ip_phone_bp)
    app.register_blueprint(location_type_bp)
    app.register_blueprint(monitor_in_workplace_bp)
    app.register_blueprint(monitor_bp)
    app.register_blueprint(office_bp)
    app.register_blueprint(position_bp)
    app.register_blueprint(printer_in_workplace_bp)
    app.register_blueprint(printer_bp)
    app.register_blueprint(router_in_workplace_bp)
    app.register_blueprint(router_bp)
    app.register_blueprint(type_bp)
    app.register_blueprint(workplace_bp)

