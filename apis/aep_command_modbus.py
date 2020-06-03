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
#参数productId: 类型String, 参数不可以为空
#  描述:
#参数searchValue: 类型String, 参数可以为空
#  描述:
#参数deviceId: 类型String, 参数可以为空
#  描述:
#参数status: 类型String, 参数可以为空
#  描述:状态可选填： 1：指令已保存 2：指令已发送 3：指令已送达 4：指令已完成 6：指令已取消 999：指令失败
#参数startTime: 类型String, 参数可以为空
#  描述:
#参数endTime: 类型String, 参数可以为空
#  描述:
#参数pageNow: 类型String, 参数可以为空
#  描述:
#参数pageSize: 类型String, 参数可以为空
#  描述:
def QueryCommandList(appKey, appSecret, MasterKey, productId, searchValue, deviceId, status, startTime, endTime, pageNow, pageSize):
    path = '/aep_command_modbus/modbus/commands'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'deviceId':deviceId, 'status':status, 'startTime':startTime, 'endTime':endTime, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20200404012458'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数commandId: 类型String, 参数不可以为空
#  描述:
#参数productId: 类型long, 参数不可以为空
#  描述:
def QueryCommand(appKey, appSecret, MasterKey, commandId, productId):
    path = '/aep_command_modbus/modbus/command'
    head = {}
    param = {'commandId':commandId, 'productId':productId}
    version = '20200404012456'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CancelCommand(appKey, appSecret, MasterKey, body):
    path = '/aep_command_modbus/modbus/cancelCommand'
    head = {}
    param = {}
    version = '20200404012453'
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
def CreateCommand(appKey, appSecret, MasterKey, body):
    path = '/aep_command_modbus/modbus/command'
    head = {}
    param = {}
    version = '20200404012449'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

