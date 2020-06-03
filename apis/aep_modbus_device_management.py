#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数MasterKey: 类型String, 参数不可以为空
#  描述:
#参数deviceId: 类型String, 参数不可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateDevice(appKey, appSecret, MasterKey, deviceId, body):
    path = '/aep_modbus_device_management/modbus/device'
    head = {}
    param = {'deviceId':deviceId}
    version = '20200404012440'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateDevice(appKey, appSecret, body):
    path = '/aep_modbus_device_management/modbus/device'
    head = {}
    param = {}
    version = '20200404012437'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数deviceId: 类型String, 参数不可以为空
#  描述:
#参数productId: 类型long, 参数不可以为空
#  描述:
def QueryDevice(appKey, appSecret, MasterKey, deviceId, productId):
    path = '/aep_modbus_device_management/modbus/device'
    head = {}
    param = {'deviceId':deviceId, 'productId':productId}
    version = '20200404012435'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数productId: 类型long, 参数不可以为空
#  描述:
#参数searchValue: 类型String, 参数可以为空
#  描述:设备名称，设备编号，设备Id
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def QueryDeviceList(appKey, appSecret, MasterKey, productId, searchValue, pageNow, pageSize):
    path = '/aep_modbus_device_management/modbus/devices'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20200404012428'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数productId: 类型long, 参数不可以为空
#  描述:
#参数deviceIds: 类型String, 参数不可以为空
#  描述:
def DeleteDevice(appKey, appSecret, MasterKey, productId, deviceIds):
    path = '/aep_modbus_device_management/modbus/device'
    head = {}
    param = {'productId':productId, 'deviceIds':deviceIds}
    version = '20200404012425'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

