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





