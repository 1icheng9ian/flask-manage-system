#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
def QueryRemoteUpgradeDetail(appKey, appSecret, id, productId, MasterKey):
    path = '/aep_upgrade_management/detail'
    head = {}
    param = {'id':id, 'productId':productId}
    version = '20190615001517'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
def QueryRemoteUpgradeTask(appKey, appSecret, id, productId, MasterKey):
    path = '/aep_upgrade_management/task'
    head = {}
    param = {'id':id, 'productId':productId}
    version = '20190615001509'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def ControlRemoteUpgradeTask(appKey, appSecret, id, MasterKey, body):
    path = '/aep_upgrade_management/control'
    head = {}
    param = {'id':id}
    version = '20190615001456'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数id: 类型String, 参数可以为空
#  描述:主任务id,isSelectDevice为1时必填，为2不必填
#参数productId: 类型String, 参数不可以为空
#  描述:产品id
#参数isSelectDevice: 类型String, 参数不可以为空
#  描述:查询类型（1.查询加入升级设备，2.查询可加入升级设备）
#参数pageNow: 类型String, 参数可以为空
#  描述:当前页，默认1
#参数pageSize: 类型String, 参数可以为空
#  描述:每页显示数，默认20
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
#参数deviceIdSearch: 类型String, 参数可以为空
#  描述:根据设备id精确查询
#参数deviceNameSearch: 类型String, 参数可以为空
#  描述:根据设备名称精确查询
#参数imeiSearch: 类型String, 参数可以为空
#  描述:根据imei号精确查询，仅支持LWM2M协议
#参数deviceNoSearch: 类型String, 参数可以为空
#  描述:根据设备编号精确查询，仅支持T_Link协议
#参数deviceGroupIdSearch: 类型String, 参数可以为空
#  描述:根据群组id精确查询
def QueryRemoteUpradeDeviceList(appKey, appSecret, id, productId, isSelectDevice, pageNow, pageSize, MasterKey, deviceIdSearch, deviceNameSearch, imeiSearch, deviceNoSearch, deviceGroupIdSearch):
    path = '/aep_upgrade_management/devices'
    head = {}
    param = {'id':id, 'productId':productId, 'isSelectDevice':isSelectDevice, 'pageNow':pageNow, 'pageSize':pageSize, 'deviceIdSearch':deviceIdSearch, 'deviceNameSearch':deviceNameSearch, 'imeiSearch':imeiSearch, 'deviceNoSearch':deviceNoSearch, 'deviceGroupIdSearch':deviceGroupIdSearch}
    version = '20190615001451'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数updateBy: 类型String, 参数可以为空
#  描述:修改人
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
def DeleteRemoteUpgradeTask(appKey, appSecret, id, productId, updateBy, MasterKey):
    path = '/aep_upgrade_management/task'
    head = {}
    param = {'id':id, 'productId':productId, 'updateBy':updateBy}
    version = '20190615001444'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数，默认1
#参数pageSize: 类型long, 参数可以为空
#  描述:每页显示数，默认20
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
#参数searchValue: 类型String, 参数可以为空
#  描述:查询条件，支持主任务名称模糊查询
def QueryRemoteUpgradeTaskList(appKey, appSecret, productId, pageNow, pageSize, MasterKey, searchValue):
    path = '/aep_upgrade_management/tasks'
    head = {}
    param = {'productId':productId, 'pageNow':pageNow, 'pageSize':pageSize, 'searchValue':searchValue}
    version = '20190615001440'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数MasterKey: 类型String, 参数可以为空
#  描述:
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def ModifyRemoteUpgradeTask(appKey, appSecret, id, MasterKey, body):
    path = '/aep_upgrade_management/task'
    head = {}
    param = {'id':id}
    version = '20190615001433'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateRemoteUpgradeTask(appKey, appSecret, MasterKey, body):
    path = '/aep_upgrade_management/task'
    head = {}
    param = {}
    version = '20190615001416'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def OperationalRemoteUpgradeTask(appKey, appSecret, MasterKey, body):
    path = '/aep_upgrade_management/operational'
    head = {}
    param = {}
    version = '20190615001412'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数taskStatus: 类型long, 参数可以为空
#  描述:子任务状态
#       T-Link协议必填（1.待升级，2.升级中，3.升级成功，4.升级失败）
#       LWM2M协议选填（0:升级可行性判断,1:升级可行性判断失败,2:分派升级任务,3:分派升级任务失败,4:分派下载任务,5:分派下载任务失败,6:开始升级,7:升级失败,8:升级完成,9:取消当前设备的升级,10:取消当前设备升级成功,11:取消当前设备升级失败）
#参数searchValue: 类型String, 参数可以为空
#  描述:查询值，设备ID或设备编号(IMEI)或设备名称模糊查询
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页码
#参数pageSize: 类型long, 参数可以为空
#  描述:每页显示数
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
def QueryRemoteUpgradeSubtasks(appKey, appSecret, id, productId, taskStatus, searchValue, pageNow, pageSize, MasterKey):
    path = '/aep_upgrade_management/details'
    head = {}
    param = {'id':id, 'productId':productId, 'taskStatus':taskStatus, 'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190615001406'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

