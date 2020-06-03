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
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateCommand(appKey, appSecret, MasterKey, body):
    path = '/aep_device_command/command'
    head = {}
    param = {}
    version = '20190712225145'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数productId: 类型long, 参数不可以为空
#  描述:
#参数searchValue: 类型String, 参数可以为空
#  描述:LWM2M协议可选填:IMEI号，指令Id
#       TUP协议可选填:IMEI号，指令Id
#       T-link协议可选填:设备编号，指令Id
#       MQTT协议可选填:设备编号，指令Id
#参数deviceId: 类型String, 参数可以为空
#  描述:
#参数status: 类型long, 参数可以为空
#  描述:状态可选填：
#       1：指令已保存
#       2：指令已发送
#       3：指令已送达
#       4：指令已完成
#       6：指令已取消
#       999：指令发送失败
#参数startTime: 类型String, 参数可以为空
#  描述:精确到毫秒的时间戳
#参数endTime: 类型String, 参数可以为空
#  描述:精确到毫秒的时间戳
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数，最大40
#参数groupCommandId: 类型String, 参数可以为空
#  描述:群组任务ID
def QueryCommandList(appKey, appSecret, MasterKey, productId, searchValue, deviceId, status, startTime, endTime, pageNow, pageSize, groupCommandId):
    path = '/aep_device_command/commands'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'deviceId':deviceId, 'status':status, 'startTime':startTime, 'endTime':endTime, 'pageNow':pageNow, 'pageSize':pageSize, 'groupCommandId':groupCommandId}
    version = '20190712225211'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数commandId: 类型String, 参数不可以为空
#  描述:创建指令成功响应中返回的id，
#参数productId: 类型long, 参数不可以为空
#  描述:
#参数deviceId: 类型String, 参数可以为空
#  描述:设备ID，Lwm2m协议必填
def QueryCommand(appKey, appSecret, MasterKey, commandId, productId, deviceId):
    path = '/aep_device_command/command'
    head = {}
    param = {'commandId':commandId, 'productId':productId, 'deviceId':deviceId}
    version = '20190712225241'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CancelCommand(appKey, appSecret, MasterKey, body):
    path = '/aep_device_command/cancelCommand'
    head = {}
    param = {}
    version = '20190615023142'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

