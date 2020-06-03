#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数productId: 类型long, 参数不可以为空
#  描述:产品ID
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey
def ProductGetInfo(appKey, appSecret, productId, MasterKey):
    path = '/aep_product/dm/product/v1/product'
    head = {}
    param = {'productId':productId}
    version = '20180717135002'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

