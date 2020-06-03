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
#  描述:固件id
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateFirmware(appKey, appSecret, id, MasterKey, body):
    path = '/aep_firmware_management/firmware'
    head = {}
    param = {'id':id}
    version = '20190615001705'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数searchValue: 类型String, 参数可以为空
#  描述:查询条件，可以根据固件名称模糊查询
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
#参数MasterKey: 类型String, 参数可以为空
#  描述:
def QueryFirmwareList(appKey, appSecret, productId, searchValue, pageNow, pageSize, MasterKey):
    path = '/aep_firmware_management/firmwares'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190615001608'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:固件id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
def QueryFirmware(appKey, appSecret, id, productId, MasterKey):
    path = '/aep_firmware_management/firmware'
    head = {}
    param = {'id':id, 'productId':productId}
    version = '20190618151645'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:固件id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数updateBy: 类型String, 参数可以为空
#  描述:修改人
#参数MasterKey: 类型String, 参数可以为空
#  描述:MasterKey
def DeleteFirmware(appKey, appSecret, id, productId, updateBy, MasterKey):
    path = '/aep_firmware_management/firmware'
    head = {}
    param = {'id':id, 'productId':productId, 'updateBy':updateBy}
    version = '20190615001534'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

