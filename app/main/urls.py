from flask import Blueprint
from . import views, errors

main = Blueprint('main', __name__)

main.add_url_rule('/index', 'index', views.index)
main.add_url_rule('/device', 'device', views.device, methods=['GET', 'POST'])
main.add_url_rule('/device/add_device', 'add_device', views.add_device, methods=['GET', 'POST'])
main.add_url_rule('/bulletin', 'bulletin', views.bulletin)
main.add_url_rule('/alarm', 'alarm', views.alarm)
main.add_url_rule('/push_port', 'push_port', views.push_port, methods=['POST'])
main.add_url_rule('/alarm/confirm_one/<id>', 'confirm_one', views.confirm_one)
main.app_context_processor(views.get_context_data)

main.errorhandler(404)(errors.page_not_found)
main.errorhandler(401)(errors.handle_unauthorized)
main.errorhandler(403)(errors.handle_forbidden)
