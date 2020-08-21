# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/18
'''

from app import db
import datetime

STATE = {'offline': '离线', 'online': '在线', 'fault': '故障'}
EVENT = {0: '下线', 1: '上线', 2: '警报', 3: '故障'}
ERROR = {1: '烟感故障', 2: '烟感故障解除', 3: '低压故障', 4: '低压故障解除'}
SERVICE = {1001: '拆除', 1002: '故障', 1003: '烟雾'}

class Device(db.Document):
    operator = db.StringField(max_length=64, required=True)
    imei = db.StringField(required=True)
    productId = db.StringField(required=True)
    productName = db.StringField()
    deviceName = db.StringField(max_length=128, required=True)
    deviceId = db.StringField()
    apiKey = db.StringField()
    autoObserver = db.BooleanField(default=0, required=True)
    createTime = db.DateTimeField(required=True)
    updateTime = db.DateTimeField()    # 和心跳周期有关
    company = db.StringField(max_length=255)
    location = db.StringField(max_length=255)
    state = db.StringField(default='offline')
    batteryValue = db.IntField(default=100)
    heartbeat_time = db.IntField(default=0)
    
class Alarm(db.Document):
    time = db.DateTimeField(required=True)
    productId = db.StringField(required=True)
    eventType = db.IntField()
    serviceId = db.IntField()
    imei = db.StringField()
    deviceId = db.StringField()
    tamper_alarm = db.IntField()    # 1-拆除 0-装上
    smoke_state = db.IntField()      # 1-解除 0-警报
    smoke_value = db.IntField()
    battery_value = db.IntField()
    error = db.IntField()
    location = db.StringField()
    deviceName = db.StringField()
    operator = db.StringField()
    read = db.BooleanField(default=False)


class Heart(db.Document):
    time = db.DateTimeField(default=datetime.datetime.now, required=True)
    imei = db.StringField(required=True)
    heartbeat_time = db.FloatField(required=True)
    battery_value = db.IntField(required=True)
    