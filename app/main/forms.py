# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/20
'''

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, ValidationError
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from .models import Device



class AddDeviceForm(FlaskForm):
    imei = StringField('imei号', validators=[DataRequired(), Length(min=15, max=15, message='请输入15位imei号!')])
    company = StringField('设备购买单位', validators=[DataRequired()])
    location = StringField('安装位置', validators=[DataRequired()])

    def validate_imei(self, field):
        if Device.objects.filter(imei=field.data).count() > 0:
            raise ValidationError('设备已添加')

'''
查询表单
class QueryDeviceForm(FlaskForm):
    imei = StringField('imei号')
'''