# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/02
配置
'''

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sadga2342rtgafga,gafefw'
    MONGODB_SETTINGS = {'db': 'Hema-test'} # 默认是本地
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
    STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': os.environ.get('DB_NAME') or 'Hema',
        'host': os.environ.get('MONGO_HOST') or 'localhost',
    }

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}