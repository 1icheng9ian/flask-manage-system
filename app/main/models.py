# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/18
'''

from app import db

STATE = {'offline': '离线', 'online': '在线', 'fault': '故障'}


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
    company = db.StringField(max_length=255)
    location = db.StringField(max_length=255)
    state = db.StringField(default='offline')
    

