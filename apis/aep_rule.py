#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def QueryRuleByRuleId(appKey, appSecret, body):
    path = '/aep_rule/rule'
    head = {}
    param = {}
    version = '20181031175724'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasUpdateRule(appKey, appSecret, body):
    path = '/aep_rule/api/v2/rule/sass/updateRule'
    head = {}
    param = {}
    version = '20190810004339'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasDeleteRuleEngine(appKey, appSecret, body):
    path = '/aep_rule/api/v2/rule/sass/deleteRule'
    head = {}
    param = {}
    version = '20190814092635'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasQueryRule(appKey, appSecret, body):
    path = '/aep_rule/api/v2/rule/sass/queryRule'
    head = {}
    param = {}
    version = '20190810004329'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasCreateRule(appKey, appSecret, body):
    path = '/aep_rule/api/v2/rule/sass/createRule'
    head = {}
    param = {}
    version = '20190814092222'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

