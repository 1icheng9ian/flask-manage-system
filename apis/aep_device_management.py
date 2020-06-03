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
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数productId: 类型long, 参数不可以为空
#  描述:
#参数searchValue: 类型String, 参数可以为空
#  描述:T-link协议可选填:设备名称，设备编号，设备Id
#       MQTT协议可选填:设备名称，设备编号，设备Id
#       LWM2M协议可选填:设备名称，设备Id ,IMEI号
#       TUP协议可选填:设备名称，设备Id ,IMEI号
#       TCP协议可选填:设备名称，设备编号，设备Id
#       HTTP协议可选填:设备名称，设备编号，设备Id
#       JT/T808协议可选填:设备名称，设备编号，设备Id
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数,最大40
def QueryDeviceList(appKey, appSecret, MasterKey, productId, searchValue, pageNow, pageSize):
    path = '/aep_device_management/devices'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190507012134'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
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
    path = '/aep_device_management/device'
    head = {}
    param = {'deviceId':deviceId, 'productId':productId}
    version = '20181031202139'
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
#  描述:可以删除多个设备（最多支持200个设备）。多个设备id，中间以逗号 "," 隔开 。样例：05979394b88a45b0842de729c03d99af,06106b8e1d5a458399326e003bcf05b4
def DeleteDevice(appKey, appSecret, MasterKey, productId, deviceIds):
    path = '/aep_device_management/device'
    head = {}
    param = {'productId':productId, 'deviceIds':deviceIds}
    version = '20181031202131'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:
#参数deviceId: 类型String, 参数不可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateDevice(appKey, appSecret, MasterKey, deviceId, body):
    path = '/aep_device_management/device'
    head = {}
    param = {'deviceId':deviceId}
    version = '20181031202122'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateDevice(appKey, appSecret, MasterKey, body):
    path = '/aep_device_management/device'
    head = {}
    param = {}
    version = '20181031202117'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def BindDevice(appKey, appSecret, MasterKey, body):
    path = '/aep_device_management/bindDevice'
    head = {}
    param = {}
    version = '20191024140057'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UnbindDevice(appKey, appSecret, MasterKey, body):
    path = '/aep_device_management/unbindDevice'
    head = {}
    param = {}
    version = '20191024140103'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数imei: 类型String, 参数不可以为空
#  描述:
def QueryProductInfoByImei(appKey, appSecret, imei):
    path = '/aep_device_management/device/getProductInfoFormApiByImei'
    head = {}
    param = {'imei':imei}
    version = '20191213161859'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

