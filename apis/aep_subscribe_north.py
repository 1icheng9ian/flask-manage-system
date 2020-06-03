#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数subId: 类型long, 参数不可以为空
#  描述:订阅记录id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数MasterKey: 类型String, 参数不可以为空
#  描述:产品MasterKey
def GetSubscription(appKey, appSecret, subId, productId, MasterKey):
    path = '/aep_subscribe_north/subscription'
    head = {}
    param = {'subId':subId, 'productId':productId}
    version = '20181031202033'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数productId: 类型long, 参数不可以为空
#  描述:产品ID
#参数pageNow: 类型long, 参数不可以为空
#  描述:当前页
#参数pageSize: 类型long, 参数不可以为空
#  描述:每页条数
#参数MasterKey: 类型String, 参数不可以为空
#  描述:
#参数subType: 类型long, 参数可以为空
#  描述:订阅类型
#参数searchValue: 类型String, 参数可以为空
#  描述:检索deviceId,模糊匹配
def GetSubscriptionsList(appKey, appSecret, productId, pageNow, pageSize, MasterKey, subType, searchValue):
    path = '/aep_subscribe_north/subscribes'
    head = {}
    param = {'productId':productId, 'pageNow':pageNow, 'pageSize':pageSize, 'subType':subType, 'searchValue':searchValue}
    version = '20181031202027'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数subId: 类型String, 参数不可以为空
#  描述:订阅记录id
#参数deviceId: 类型String, 参数可以为空
#  描述:设备id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数subLevel: 类型long, 参数不可以为空
#  描述:订阅级别
#参数MasterKey: 类型String, 参数不可以为空
#  描述:产品MasterKey
def DeleteSubscription(appKey, appSecret, subId, deviceId, productId, subLevel, MasterKey):
    path = '/aep_subscribe_north/subscription'
    head = {}
    param = {'subId':subId, 'deviceId':deviceId, 'productId':productId, 'subLevel':subLevel}
    version = '20181031202023'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateSubscription(appKey, appSecret, MasterKey, body):
    path = '/aep_subscribe_north/subscription'
    head = {}
    param = {}
    version = '20181031202018'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

