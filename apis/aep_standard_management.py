#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数standardVersion: 类型String, 参数可以为空
#  描述:标准物模型版本号
#参数thirdType: 类型long, 参数不可以为空
#  描述:三级分类Id
def QueryStandardModel(appKey, appSecret, standardVersion, thirdType):
    path = '/aep_standard_management/standardModel'
    head = {}
    param = {'standardVersion':standardVersion, 'thirdType':thirdType}
    version = '20190713033424'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

