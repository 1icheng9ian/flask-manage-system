# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/27
'''

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length
from .super_models import PublicProduct

class EditAdminInfoForm(FlaskForm):
    appkey = StringField('appkey', validators=[DataRequired()])
    appsecret = StringField('appsecret', validators=[DataRequired()])

class AddPublicProductForm(FlaskForm):
    productId = StringField('产品Id', validators=[DataRequired()])
    
    # 额外的验证以 validate_ 开头的方法会随着 validate_on_submit 一同验证
    def validate_productId(self, field):
        if PublicProduct.objects.filter(productId=field.data).count() > 0:
            raise ValidationError('请勿重复添加')

class EditBulletinForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired(), Length(max=512)])


class QueryUserForm(FlaskForm):
    username = StringField('用户名')

