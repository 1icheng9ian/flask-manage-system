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
#  描述:可填值：设备Id
#参数eventType: 类型long, 参数可以为空
#  描述:LWM2M,MQTT,TUP协议可选填:
#       1：信息
#       2：警告
#       3：故障
#       T-link协议可选填:
#       0:普通事件
#       1：告警事件(普通级)
#       2：告警事件(重大级)
#       3：告警事件(严重级)
#参数startTime: 类型String, 参数可以为空
#  描述:精确到毫秒的时间戳
#参数endTime: 类型String, 参数可以为空
#  描述:精确到毫秒的时间戳
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
def QueryEventList(appKey, appSecret, MasterKey, productId, searchValue, eventType, startTime, endTime, pageNow, pageSize):
    path = '/aep_device_event/events'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'eventType':eventType, 'startTime':startTime, 'endTime':endTime, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190507012824'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

