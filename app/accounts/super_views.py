# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/24
'''
import datetime
from json import loads

from flask import (current_app, flash, redirect, render_template, request,
                   url_for)
from flask.views import MethodView
from flask_login import current_user, login_required, login_user
from flask_principal import Identity, identity_changed

from apis.aep_device_management import DeleteDevice
from apis.aep_product_management import DeleteProduct, QueryProduct

from ..main import models as Mainmodels
from . import models, super_models
from .forms import SuperLoginForm
from .permissions import super_admin_Permission
from .super_forms import (AddPublicProductForm, EditAdminInfoForm,
                          EditBulletinForm, QueryUserForm)
from .super_models import PROTOCOL


def login():
    '''
    超级用户登录界面
    '''
    form = SuperLoginForm()
    # 验证输入的信息
    if form.validate_on_submit():
        try:
            user = models.User.objects.get(username=form.username.data)
        except models.User.DoesNotExist:
            user = None
        if user and user.verify_password(form.password.data):
            if user.role == 'super_admin':
                login_user(user)
                user.last_login_time = datetime.datetime.now
                user.save()
                identity_changed.send(current_app._get_current_object(), identity=Identity(user.username))
                return redirect(url_for('super_admin.device'))
            else:
                flash('该账号为普通账号，请从普通管理员入口登录！', 'warning')
            flash('用户名或密码错误', 'danger')
    return render_template('super_admin/login.html', form=form)

@login_required
def super_user():
    return render_template('super_admin/super_user.html')

@login_required
def super_user_edit():
    form = EditAdminInfoForm()
    if form.validate_on_submit():
        user = current_user
        user.appkey = form.appkey.data
        user.appsecret = form.appsecret.data
        user.save()
        return redirect(url_for('super_admin.super_user'))
    return render_template('super_admin/super_user_edit.html', form=form)

class UserInfo(MethodView):
    template_name = 'super_admin/userinfo.html'
    decorators = [login_required, super_admin_Permission.require(401)]

    def get(self):
        users = models.User.objects.filter(role='admin')
        try:
            cur_page = int(request.args.get('page', 1))
        except:
            cur_page = 1
        users = users.paginate(page=cur_page, per_page=10)
        data = {'users': users}
        return render_template(self.template_name, **data)

@login_required
def product_management():
    '''
    添加公司的产品public product，之后其他用户可以直接选取
    普通用户不需要知道productId
    直接输入imei就完事了
    '''
    form = AddPublicProductForm()

    if form.validate_on_submit():
        public_product = super_models.PublicProduct()
        productId = form.productId.data
        # acquire current user infomation
        user = current_user
        if not user.appkey:
            flash('出错了！请先添加appkey和appsecret!', 'warning')
        else:
            appkey = user.appkey
            appsecret = user.appsecret
            public_product.productId = form.productId.data
            # aep平台验证
            result = QueryProduct(appKey=appkey, appSecret=appsecret, productId=productId)
            result = loads(result.decode('UTF-8'))
            # 需要考虑到用户输错的情况
            if result['code'] == 0:
                public_product.productName = result['result']['productName']
                public_product.tupDeviceModel = result['result']['tupDeviceModel']
                public_product.apiKey = result['result']['apiKey']
                public_product.productProtocol = PROTOCOL[result['result']['productProtocol']] # 数字对应的协议
                public_product.productTypeValue = result['result']['productTypeValue']
                public_product.secondaryTypeValue = result['result']['secondaryTypeValue']
                public_product.thirdTypeValue = result['result']['thirdTypeValue']
                public_product.save()   # 保存
                flash('添加成功', 'success')
                return redirect(url_for('super_admin.product_management'))
            else:
                flash(result['msg'], 'warning') # 使用aep平台的error message
    # acquire data
    public_products = super_models.PublicProduct.objects.all()
    data = {'public_products': public_products}
    return render_template('super_admin/product_management.html', form=form, **data)

@login_required
def delete_public_product(productId):
    # 危险操作
    # 这里进行删除操作的时候加上询问框
    # 删除只需要从数据库中删除，aep平台不需要
    # 如果下面有产品，不能删除
    # 这里查询device count的方法是向aep平台发送一条查询指令
    # 这可能会带来一些问题，如直接在平台添加的设备，会查找不到
    # 如后期aep平台按查询次数收费，可以酌情修改
    this_product = super_models.PublicProduct.objects.get_or_404(productId=productId)
    user = current_user
    appkey = user.appkey
    appsecret = user.appsecret
    result = QueryProduct(appKey=appkey, appSecret=appsecret, productId=productId)
    result = loads(result.decode('UTF-8'))
    if result['result']['deviceCount'] == 0:
        this_product.delete()
    else:
        flash('该产品下还有设备, 禁止删除!', 'danger')
    return redirect(url_for('super_admin.product_management'))

@login_required
def device():
    devices = Mainmodels.Device.objects.all()
    form = QueryUserForm()
    if form.validate_on_submit():
        username = form.username.data
        devices = Mainmodels.Device.objects.filter(operator=username).order_by('operator')
    
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    devices = devices.paginate(page=cur_page, per_page=10)

    data = {'devices': devices}
    return render_template('super_admin/device.html', **data, form=form)


@login_required
def delete_many_devices():  # 批量删除
    deviceIds = request.values.getlist("array")
    if deviceIds:
        # 如果是全部一样的产品可以一条命令删除，如果不是，则需要分别删除
        # 所以循环删除
        history = super_models.History()    # 操作历史
        appkey = models.User.objects.get_or_404(role='super_admin').appkey
        appsecret = models.User.objects.get_or_404(role='super_admin').appsecret
        for deviceId in deviceIds:
            this_device = Mainmodels.Device.objects.get_or_404(deviceId=deviceId)
            operator = this_device.operator
            company = this_device.company
            productName = this_device.productName
            deviceName = this_device.deviceName

            result = DeleteDevice(appkey, appsecret, this_device.apiKey, this_device.productId, this_device.deviceId)
            result = loads(result.decode('UTF-8'))

            if result['code'] == 0:
                this_device.delete()

                history.operationTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                history.operator = operator
                history.company = company
                history.productName = productName
                history.deviceName = deviceName
                history.operation = 'del'
                
            else:
                flash(result['msg'], 'warning')
        history.save()
    else:
        flash('没有选择任何设备', 'warning')
    return redirect(url_for('super_admin.device'))


class History(MethodView):
    template_name = 'super_admin/history.html'
    decorators = [login_required, super_admin_Permission.require(401)]

    def get(self):
        histories = super_models.History.objects.all().order_by('-operationTime')

        try:
            cur_page = int(request.args.get('page', 1))
        except:
            cur_page = 1

        histories = histories.paginate(page=cur_page, per_page=10)

        data = {'histories': histories}
        return render_template(self.template_name, **data)

class Bulletin(MethodView):
    template_name = 'super_admin/super_bulletin.html'
    decorators = [login_required, super_admin_Permission.require(401)]

    def get(self):
        notices = super_models.Bulletin.objects.all().order_by('-time')
        try:
            cur_page = int(request.args.get('page', 1))
        except:
            cur_page = 1
        notices = notices.paginate(page=cur_page, per_page=5)
        data = {'notices': notices}
        return render_template(self.template_name, **data)

@login_required
def edit_bulletin():
    form = EditBulletinForm()
    if form.validate_on_submit():
        board = super_models.Bulletin()
        board.title = form.title.data
        board.content = form.content.data
        board.author = current_user.username
        board.save()
        return redirect(url_for('super_admin.super_bulletin'))
    return render_template('super_admin/edit_bulletin.html', form=form)
