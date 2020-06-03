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
#  描述:可填值：属性名称，属性标识符
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
def QueryPropertyList(appKey, appSecret, MasterKey, productId, searchValue, pageNow, pageSize):
    path = '/aep_device_model/dm/app/model/properties'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190712223330'
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
#  描述:可填： 服务Id, 服务名称,服务标识符
#参数serviceType: 类型long, 参数可以为空
#  描述:服务类型
#       1. 数据上报 
#       2. 事件上报 
#       3.数据获取 
#       4.参数查询 
#       5.参数配置
#       6.指令下发 
#       7.指令下发响应
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
def QueryServiceList(appKey, appSecret, MasterKey, productId, searchValue, serviceType, pageNow, pageSize):
    path = '/aep_device_model/dm/app/model/services'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'serviceType':serviceType, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190712224233'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

