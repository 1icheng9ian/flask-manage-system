#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数cardId: 类型String, 参数不可以为空
#  描述:定位的物联网卡号
#参数posReqType: 类型long, 参数不可以为空
#  描述:返回的位置类型：1为初始位置；2为最新位置；3为最新or历史位置；7目前未用到，保留数字
def getPosition(appKey, appSecret, cardId, posReqType):
    path = '/aep_gateway_position/api/getPosition'
    head = {}
    param = {'cardId':cardId, 'posReqType':posReqType}
    version = '20190301085737'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

