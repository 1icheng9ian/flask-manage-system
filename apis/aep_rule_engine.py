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
def saasCreateRule(appKey, appSecret, body):
    path = '/aep_rule_engine/api/v2/rule/sass/createRule'
    head = {}
    param = {}
    version = '20200111000503'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数ruleId: 类型String, 参数可以为空
#  描述:
#参数productId: 类型String, 参数可以为空
#  描述:
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def saasQueryRule(appKey, appSecret, ruleId, productId, pageNow, pageSize):
    path = '/aep_rule_engine/api/v2/rule/sass/queryRule'
    head = {}
    param = {'ruleId':ruleId, 'productId':productId, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20200111000633'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasUpdateRule(appKey, appSecret, body):
    path = '/aep_rule_engine/api/v2/rule/sass/updateRule'
    head = {}
    param = {}
    version = '20200111000540'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def saasDeleteRuleEngine(appKey, appSecret, body):
    path = '/aep_rule_engine/api/v2/rule/sass/deleteRule'
    head = {}
    param = {}
    version = '20200111000611'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

