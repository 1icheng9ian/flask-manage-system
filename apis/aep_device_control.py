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
#  描述:可选填：设备Id
#参数type: 类型long, 参数可以为空
#  描述:可选填枚举值：
#       1：设备重启
#       2：退出平台
#       3：重新登录
#       4：设备自检
#       6：开始发送数据
#       7：停止发送数据
#       8：恢复出厂设置
#参数status: 类型long, 参数可以为空
#  描述:可选填：1：指令已保存
#       2：指令已发送
#       3：指令已送达
#       4：指令已完成
#       999：指令发送失败
#参数startTime: 类型String, 参数可以为空
#  描述:精确到毫秒的时间戳
#参数endTime: 类型String, 参数可以为空
#  描述:精确到毫秒的时间戳
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
def QueryRemoteControlList(appKey, appSecret, MasterKey, productId, searchValue, type, status, startTime, endTime, pageNow, pageSize):
    path = '/aep_device_control/controls'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'type':type, 'status':status, 'startTime':startTime, 'endTime':endTime, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190507012630'
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
def CreateRemoteControl(appKey, appSecret, MasterKey, body):
    path = '/aep_device_control/control'
    head = {}
    param = {}
    version = '20181031202247'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

