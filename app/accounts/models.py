# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/07
'''

from flask_login import UserMixin
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

ROLES = (('admin', '管理员'), ('super_admin', '超级管理员'))

# 定义分类文档
class User(UserMixin, db.Document):
    username = db.StringField(max_length=255, required=True)    # 用户名
    wechatname = db.StringField() # 绑定的微信名
    password_hash = db.StringField(required=True)
    create_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    last_login_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    role = db.StringField(default='admin', required=True, choices=ROLES)
    appkey = db.StringField()
    appsecret = db.StringField()
    cellphone = db.StringField()
    company = db.StringField()
    address = db.StringField()

    # 密码加密解密
    @property  # 把方法变成属性调用
    def password(self):
        raise  AttributeError('没有权限查看密码')

    @password.setter
    def password(self, password):
        # 密码加密
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # 密码解密
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        try:
            return self.username
        except AttributeError:
            raise NotImplementedError('No `username` attribute - override `get_id`')

    def __unicode__(self):
        return self.username

@login_manager.user_loader
def load_user(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    return user


