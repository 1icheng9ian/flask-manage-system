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
def createOrder(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/create'
    head = {}
    param = {}
    version = '20190822094523'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def createRenewOrder(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/renew'
    head = {}
    param = {}
    version = '20190822094527'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def renewPrice(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/renewPrice'
    head = {}
    param = {}
    version = '20190822094532'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def orderCanceApply(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/orderCanceApply'
    head = {}
    param = {}
    version = '20190822094516'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def pay(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/pay'
    head = {}
    param = {}
    version = '20190822094538'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def refundInfo(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/refundInfo'
    head = {}
    param = {}
    version = '20190822094544'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def createRefundOrder(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/refund/order'
    head = {}
    param = {}
    version = '20190822094553'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def price(appKey, appSecret, body):
    path = '/aep_order/aeporder/order/v1/price'
    head = {}
    param = {}
    version = '20190822094559'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

