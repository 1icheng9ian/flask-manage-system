'''
Functions
'''
from apis import aep_product_management
from apis import aep_device_status
from urllib import error
from json import loads, dumps
from time import localtime, strftime

def CheckAccess(appKey:str, appSecret:str):
    '''
    验证账号是否有效
    '''
    try:
        aep_product_management.QueryProductList(appKey, appSecret, '', 1, 40)
    except error.HTTPError as e:
        if e.code == 404:
            return('用户名不存在')
        elif e.code == 401:
            return('密码错误')
        else:
            return('网络错误')
    else:
        return('登录成功')

def StateListener(appKey:str, appSecret:str, productId:int, deviceId:str, stateName:str):
    '''
    状态监听器
    '''
    body = dumps({'productId':productId, 'deviceId':deviceId, 'datasetId':stateName})
    result = aep_device_status.QueryDeviceStatus(appKey, appSecret, body)
    r = loads(result.decode('UTF-8'))
    value = r['deviceStatus']['value']
    timeStamp = r['deviceStatus']['timestamp']
    localTime = localtime(timeStamp / 1000)
    dataTime = strftime('%Y/%m/%d %H:%M:%S', localTime)
    return dataTime, value



