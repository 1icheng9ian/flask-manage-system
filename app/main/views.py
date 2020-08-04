# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/06
'''

from json import loads, dumps

from flask import flash, redirect, render_template, url_for, jsonify, request
from flask_login import current_user, login_required
from mongoengine.queryset.visitor import Q
from apis.aep_device_management import CreateDevice, DeleteDevice

from ..accounts.models import User
from . import models
from .forms import AddDeviceForm, QueryDeviceForm
from ..accounts import super_models, models as Usermodels
import datetime

@login_required
def index():
    # 默认添加后就是离线状态
    device_offline = models.Device.objects(Q(state='offline') & Q(operator=current_user.username)).count()
    device_online = models.Device.objects.filter(Q(state='online') & Q(operator=current_user.username)).count()
    device_fault = models.Device.objects.filter(Q(state='fault') & Q(operator=current_user.username)).count()
    # 如何判断上线状态是个问题
    # 需要结合报警那块
    data = {'device_online': device_online, 'device_offline': device_offline, 'device_fault': device_fault}
    
    return render_template('main/index.html', **data)

@login_required
def device():
    devices = models.Device.objects.filter(operator=current_user.username)
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    devices = devices.paginate(page=cur_page, per_page=10)
    
    form = QueryDeviceForm()    # 查询表单
    if form.validate_on_submit():
        imei = form.imei.data

    data = {'devices': devices}
    return render_template('main/device.html', form=form, **data)

@login_required
def add_device():
    # 首先选择公共产品
    # 单选框
    public_products = super_models.PublicProduct.objects.all()
    data = {'public_products': public_products}

    form = AddDeviceForm()
    if form.validate_on_submit():
        # database
        device = models.Device()
        history = super_models.History()    # 添加操作历史
        # operator is current user
        device.operator = current_user.username
        device.imei = form.imei.data
        device.productId = request.values.get('productId')
        productId = request.values.get('productId')
        public_info = super_models.PublicProduct.objects.get_or_404(productId=productId)
        device.productName = public_info.productName
        # productName = public_info.productName
        device.apiKey = public_info.apiKey
        apiKey = public_info.apiKey
        # deviceName is the location
        device.deviceName = form.location.data
        device.location = form.location.data
        device.company = form.company.data
        # 自动订阅设置
        device.autoObserver = form.autoObserver.data
        if not form.autoObserver.data:
            autoObserver = 1
        else:
            autoObserver = 0
        
        # deviceId 在aep平台注册成功后获取
        # 该用户用的公共产品
        appkey = Usermodels.User.objects.get_or_404(role='super_admin').appkey
        appsecret = Usermodels.User.objects.get_or_404(role='super_admin').appsecret
        body = dumps({
            "deviceName": device.deviceName,
            "imei": device.imei,
            "operator": device.operator,
            "other": {"autoObserver": autoObserver},
            "productId": productId
        })
        result = CreateDevice(appkey, appsecret, apiKey, body)
        result = loads(result.decode('UTF-8'))
        if result['code'] == 0:
            device.deviceId = result['result']['deviceId']
            # 时间不能在models中直接填入，会出现问题
            device.createTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            device.save()
            # 保存操作历史
            history.operationTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            history.operator = current_user.username
            history.company = form.company.data
            history.productName = public_info.productName
            history.deviceName = form.location.data
            history.operation = 'add'
            history.save()
            flash('添加成功', 'success')
        else:
            flash(result['msg'], 'warning')

    return render_template('main/add_device.html', form=form, **data)

@login_required
def delete_device(imei):
    this_device = models.Device.objects.get_or_404(imei=imei)
    # 变量提取
    company = this_device.company
    productName = this_device.productName
    deviceName = this_device.deviceName

    history = super_models.History()    # 操作历史
    
    appkey = Usermodels.User.objects.get_or_404(role='super_admin').appkey
    appsecret = Usermodels.User.objects.get_or_404(role='super_admin').appsecret
    result = DeleteDevice(appkey, appsecret, this_device.apiKey, this_device.productId, this_device.deviceId)
    result = loads(result.decode('UTF-8'))
    if result['code'] == 0:
        this_device.delete()

        history.operationTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        history.operator = current_user.username
        history.company = company
        history.productName = productName
        history.deviceName = deviceName
        history.operation = 'del'
        history.save()

        return redirect(url_for('main.device'))
    else:
        flash(result['msg'], 'warning')


@login_required
def bulletin():
    notices = super_models.Bulletin.objects.all()
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    notices = notices.paginate(page=cur_page, per_page=5)
    data = {'notices': notices}
    return render_template('main/bulletin.html', **data)


@login_required
def alarm():
    return render_template('main/alarm.html')