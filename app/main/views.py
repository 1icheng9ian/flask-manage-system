# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/06
'''

from json import loads, dumps

from flask import flash, redirect, render_template, url_for, request, session
from flask_login import current_user, login_required
from mongoengine.queryset.visitor import Q
from apis.aep_device_management import CreateDevice, DeleteDevice

from ..accounts.models import User
from . import models
from .forms import AddDeviceForm, QueryDeviceForm
from ..accounts import super_models, models as Usermodels
import datetime, time
from flask.views import MethodView

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
    # 表格显示部分
    message = ''
    devices = models.Device.objects.filter(operator=current_user.username).order_by('-createTime')
    all_devices = devices
    form = QueryDeviceForm()    # 表单部分
    # 用户可以进行模糊搜索
    # 可以只选择三个中的一个
    # 如果填写了多个，默认就是复合搜索
    # 如果找不到，需要给出warning
    if form.validate_on_submit():
        imei = form.imei.data
        company = form.company.data
        state = request.values.get('state')
        message = '当前查找条件:' + imei + company
        if state == 'all':
            if imei and company:
                devices = models.Device.objects(Q(imei=imei) & Q(company=company)).filter(operator=current_user.username).order_by('-createTime')
            elif imei and not company:
                devices = models.Device.objects(Q(imei=imei)).filter(operator=current_user.username).order_by('-createTime')
            elif not imei and company:
                devices = models.Device.objects(Q(company=company)).filter(operator=current_user.username).order_by('-createTime')
            else:
                devices = all_devices
        else:
            if imei and company:
                devices = models.Device.objects(Q(imei=imei) & Q(company=company) & Q(state=state)).filter(operator=current_user.username).order_by('-createTime')
            elif imei and not company:
                devices = models.Device.objects(Q(imei=imei) & Q(state=state)).filter(operator=current_user.username).order_by('-createTime')
            elif not imei and company:
                devices = models.Device.objects(Q(company=company) & Q(state=state)).filter(operator=current_user.username).order_by('-createTime')
            else:
                devices = models.Device.objects(Q(state=state)).filter(operator=current_user.username).order_by('-createTime')

    # 判断设备是否离线
    endtime = datetime.datetime.now()
    for device in devices:
        if not device.updateTime:
            device.state = 'offline'
        else:
            starttime = device.updateTime
            heartTime = device.heartbeat_time
            second = (endtime - starttime).seconds
            if second > heartTime:
                device.state = 'offline'

    # 分页
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    devices = devices.paginate(page=cur_page, per_page=10)

    data = {'devices': devices, 'message': message}
    return render_template('main/device.html', **data, form=form)


@login_required
def add_device():
    # 首先选择公共产品
    # 单选框
    public_products = super_models.PublicProduct.objects.all()
    if not public_products:
        flash('产品库中没有产品，请联系超级管理员！', 'warning')
    data = {'public_products': public_products}

    form = AddDeviceForm()
    if form.validate_on_submit():
        # database
        device = models.Device()
        history = super_models.History()    # 添加操作历史
        # operator is current user
        device.operator = current_user.username
        device.imei = form.imei.data
        productId = request.values.get('productId')
        device.productId = request.values.get('productId')
        public_info = super_models.PublicProduct.objects.get_or_404(productId=productId)
        device.productName = public_info.productName
        # productName = public_info.productName
        device.apiKey = public_info.apiKey
        apiKey = public_info.apiKey
        # deviceName is the location
        device.deviceName = form.location.data
        device.location = form.location.data
        device.company = form.company.data
        # 自动订阅设置, 必须是ture
        device.autoObserver = True
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
def bulletin():
    notices = super_models.Bulletin.objects.all().order_by('-time')
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    notices = notices.paginate(page=cur_page, per_page=5)
    data = {'notices': notices}
    return render_template('main/bulletin.html', **data)


@login_required
def alarm():
    alarms = models.Alarm.objects.filter(operator=current_user.username).order_by('-time')
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    alarms = alarms.paginate(page=cur_page, per_page=9)
    data = {'alarms': alarms}
    return render_template('main/alarm.html', **data)

@login_required
def confirm_one(id):
    '''处理单个报警信息: 将read属性改为True，并将按钮变灰'''
    this_alarm = models.Alarm.objects.get_or_404(id=id)
    this_alarm.read = True
    this_alarm.save()
    
    alarms = models.Alarm.objects.filter(operator=current_user.username).order_by('-time')
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    alarms = alarms.paginate(page=cur_page, per_page=9)
    data = {'alarms': alarms}
    return render_template('main/alarm.html', **data)

def confirm_many():
    '''批量处理'''
    pass

def push_port():
    if request.data:
        msg = request.data.decode('utf-8')
        msg = loads(msg)
        # 存进数据库
        if 'timestamp' in msg:
            alarm = models.Alarm()
            alarm.productId = msg['productId']
            alarm.deviceId = msg['deviceId']
            # 对应的设备信息
            this_device = models.Device.objects.get_or_404(deviceId=msg['deviceId'])
            alarm.location = this_device.location
            alarm.deviceName = this_device.deviceName
            alarm.operator = this_device.operator
            
            time = datetime.datetime.fromtimestamp(msg['timestamp'] / 1000)
            alarm.time = time.strftime('%Y-%m-%d %H:%M:%S')
            eventType = msg['eventType']
            if eventType == 1:  # 上线
                alarm.eventType = eventType
                # 改变这个设备的状态
                this_device.state = 'online'

            elif eventType == 0:    # 下线
                alarm.eventType = eventType
                this_device.state = 'offline'

            else:
                alarm.imei = msg['IMEI']
                serviceId = msg['serviceId']

                if eventType == 2 and serviceId == 1003:
                    alarm.smoke_state = msg['eventContent']['smoke_state']
                    alarm.smoke_value = msg['eventContent']['smoke_value']
                    
                elif eventType == 2 and serviceId == 1001:
                    alarm.tamper_alarm = msg['eventContent']['tamper_alarm']
                    alarm.battery_value = msg['eventContent']['battery_value']
                    this_device.batteryValue = msg['eventContent']['battery_value']

                elif eventType == 3 and serviceId == 1002:
                    alarm.error = msg['eventContent']['error']
                    this_device.state = 'fault'

                alarm.eventType = eventType
                alarm.serviceId = serviceId

            this_device.updateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 时间点
            this_device.save()
            alarm.save()
            
        else:
            heart = models.Heart()
            heart.imei = msg['IMEI']
            heart.heartbeat_time = msg['heartbeat_time']
            heartbeat_time = int(msg['heartbeat_time']) * 3600  # 心跳周期秒数
            heart.battery_value = msg['battery_value']
            heart.save()

            this_device = models.Device.objects.get_or_404(imei=msg['IMEI'])
            this_device.batteryValue = msg['battery_value'] # 修改电量
            this_device.updateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            this_device.heartbeat_time = heartbeat_time     # 存库
            this_device.save()

        return '200 OK' # 电信平台需要返回200状态


# 不能加login_required, 原因未知 
# 这样就不能用current_user的区分不同用户的报警信息了
def get_context_data():
    '''暂时这样，更好的是设置服务器端的session'''
    unread = models.Alarm.objects(read=False).count()
    return {'unread': unread}