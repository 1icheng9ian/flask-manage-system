# -*- encoding: utf-8 -*-
# 功能型函数
from json import loads

from apis.aep_device_management import CreateDevice, DeleteDevice


def AddDevice(appKey, appSecret, MasterKey, body):
    result = CreateDevice(appKey, appSecret, MasterKey, body)
    r = loads(result.decode('UTF-8'))
    return r['msg']
    
def RemoveDevice(appKey, appSecret, MasterKey, productId, deviceId):
    result = DeleteDevice(appKey, appSecret, MasterKey, productId, deviceId)
    r = loads(result.decode('UTF-8'))
    return r['msg']
