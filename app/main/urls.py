from flask import Blueprint
from . import views, errors

main = Blueprint('main', __name__)

main.add_url_rule('/index', 'index', views.index)
main.add_url_rule('/device', 'device', views.device)
main.add_url_rule('/add_device', 'add_device', views.add_device, methods=['GET', 'POST'])
main.add_url_rule('/delete_device/<string:imei>', 'delete_device', views.delete_device, methods=['GET'])