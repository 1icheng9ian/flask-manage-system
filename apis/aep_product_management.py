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
#  描述:
def QueryProduct(appKey, appSecret, productId):
    path = '/aep_product_management/product'
    head = {}
    param = {'productId':productId}
    version = '20181031202055'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数searchValue: 类型String, 参数可以为空
#  描述:产品id或者产品名称
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数，最大40
def QueryProductList(appKey, appSecret, searchValue, pageNow, pageSize):
    path = '/aep_product_management/products'
    head = {}
    param = {'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20190507004824'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey在该设备所属产品的概况中可以查看
#参数productId: 类型long, 参数不可以为空
#  描述:
def DeleteProduct(appKey, appSecret, MasterKey, productId):
    path = '/aep_product_management/product'
    head = {}
    param = {'productId':productId}
    version = '20181031202029'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateProduct(appKey, appSecret, body):
    path = '/aep_product_management/product'
    head = {}
    param = {}
    version = '20191018204154'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateProduct(appKey, appSecret, body):
    path = '/aep_product_management/product'
    head = {}
    param = {}
    version = '20191018204806'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'PUT')
    if response is not None:
        return response.read()
    return None

