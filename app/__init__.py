# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/02
初始化
'''

import os

from flask import Flask
from .config import config
from flask_login import LoginManager
from flask_moment import Moment
from flask_mongoengine import MongoEngine
from flask_principal import Principal

# 初始化
db = MongoEngine()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'accounts.login'

Principals = Principal()

def create_app(config_name):
    app = Flask(__name__, template_folder=config[config_name].TEMPLATE_PATH,
                static_folder=config[config_name].STATIC_PATH)
    
    # 导入设置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    Principals.init_app(app)

    # 这里注册蓝图
    from .main.urls import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .accounts.urls import accounts as accounts_blueprint, super_admin as super_admin_blueprint
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(super_admin_blueprint)

    return app


app = create_app(os.getenv('config') or 'default')
