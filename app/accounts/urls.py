# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/14
'''

from flask import Blueprint
from . import views, super_views
from ..main import errors

# 创建 blueprint 对象
accounts = Blueprint('accounts', __name__)

# 这里注册路由
# 路由 | 站点，url_for()反转时里面的值 | 对应的函数 | 访问规则methods
accounts.add_url_rule('/', 'login', views.login, methods=['GET', 'POST'])
accounts.add_url_rule('/register', 'register', views.register, methods=['GET', 'POST'])
accounts.add_url_rule('/user', view_func=views.User.as_view('user'))
accounts.add_url_rule('/user/update_profile', 'update_profile', views.update_profile, methods=['GET', 'POST'])
accounts.add_url_rule('/update_pass', 'update_pass', views.update_pass, methods=['GET', 'POST'])
accounts.add_url_rule('/logout', 'logout', views.logout)

super_admin = Blueprint('super_admin', __name__)

super_admin.add_url_rule('/super_login', 'login', super_views.login, methods=['GET', 'POST'])
super_admin.add_url_rule('/super_index', view_func=super_views.Index.as_view('index'))
super_admin.add_url_rule('/super/product_management', 'product_management', super_views.product_management, methods=['GET', 'POST'])
super_admin.add_url_rule('/super_user', 'super_user', super_views.super_user)
super_admin.add_url_rule('/super_user/super_user_edit', 'super_user_edit', super_views.super_user_edit, methods=['GET', 'POST'])

super_admin.add_url_rule('/super/device', view_func=super_views.Device.as_view('device'))
super_admin.add_url_rule('/super/device/delete_device/<string:imei>', 'delete_device', super_views.delete_device)

# delete 时，需要从前端传参
super_admin.add_url_rule('/product_management/delete_public_product/<string:productId>', 'delete_public_product', super_views.delete_public_product, methods=['GET'])
super_admin.add_url_rule('/history', 'history', super_views.history)
super_admin.add_url_rule('/super_bulletin', 'super_bulletin', super_views.super_bulletin)
super_admin.add_url_rule('/super_bulletin/edit_bulletin', 'edit_bulletin', super_views.edit_bulletin, methods=['GET', 'POST'])

