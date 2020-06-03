#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数sdk_type: 类型String, 参数可以为空
#  描述:SDK语言类型，默认为Java(字典项: sdk_type)
#参数file_name: 类型String, 参数不可以为空
#  描述:SDK描述，用以标识其中的biz包
#参数application_id: 类型String, 参数不可以为空
#  描述:应用编码，下载的SDK会根据该编码收集所有有权限的API打包
#参数api_version: 类型String, 参数可以为空
#  描述:API版本信息 TODO
def SdkDownload(appKey, appSecret, sdk_type, file_name, application_id, api_version):
    path = '/usr/sdk/download'
    head = {}
    param = {'sdk_type':sdk_type, 'file_name':file_name, 'application_id':application_id, 'api_version':api_version}
    version = '20180000000000'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

