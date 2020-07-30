# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/16
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
from .models import User
from .models import ROLES
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])

class SuperLoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(),
        Length(1,15),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '只能含有大小写和数字')])
    password = PasswordField('密码', validators=[
        DataRequired(),
        Length(6, 16, message='密码长度在6到12位'),
        EqualTo('password2', message='密码必须一致')
    ])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    role = SelectField('权限', choices=ROLES)

    def validate_username(self, field):
        if User.objects.filter(username=field.data).count() > 0:
            raise ValidationError('用户已注册')

class UpdateProfileForm(FlaskForm):
    cellphone = StringField('手机号')
    company = StringField('公司')
    address = StringField('地址')

class ModifyPasswordForm(FlaskForm):
    current_password = PasswordField('原密码', validators=[DataRequired()])
    new_password = PasswordField('新密码', validators=[DataRequired(),
        EqualTo('confirm_password', message='密码不一致')])
    confirm_password = PasswordField('确认新密码', validators=[DataRequired()])

    def validate_current_password(self, field):
        if not current_user.verify_password(field.data):
            raise ValidationError('新密码和原密码不一致')
