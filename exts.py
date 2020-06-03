'''
Functions
'''
from apis import aep_product_management
import json

def CheckAccess(appKey:str, appSecret:str):
    '''
    验证账号是否有效
    '''
    try:
        result = aep_product_management.QueryProductList(appKey, appSecret, '', 1, 40)
        r = json.loads(result.decode('UTF-8'))
    except:
        return '账号或密码错误'
    else:
        return '验证成功'

def QueryAllProduct(appKey:str, appSecret:str):
    '''
    查询所有产品
    '''
    result = aep_product_management.QueryProductList(appKey, appSecret, '', 1, 40)
    r = json.loads(result.decode('UTF-8'))
    rr = r['result']['list']
    return rr


def QueryOneProduct(appKey:str, appSecret:str, productID:int):
    '''
    查询特定产品
    用在搜索栏中
    '''
    result = aep_product_management.QueryProduct(appKey, appSecret, productID)
    r = json.loads(result.decode('UTF-8'))
    rr = r['result']['list']
    return rr

