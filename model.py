'''
Database: Mongodb
'''
from pymongo import MongoClient
from werkzeug.security import generate_password_hash #加密
from apis import aep_device_management
from apis import aep_product_management
from time import localtime, strftime
import json
host = '127.0.0.1'
port = 27017
dbname = 'NBdatabase'

def Connect(collname:str):
    '''
    连接数据库
    '''
    connect = MongoClient(host, port)
    db = connect[dbname]
    collection = db[collname]
    return collection

def saveaccout(appKey:str, appSecret:str):
    '''
    保存账号到数据库
    密码加密
    '''
    account =Connect('user')
    count = account.count_documents({'appKey': appKey})
    if count == 0:
        appsecret_m = generate_password_hash(appSecret)
        account.insert_one({'appKey': appKey, 'appSecret': appsecret_m})
    else:
        pass

def UpdateAllProduct(appKey:str, appSecret:str):
    '''
    更新所有产品
    '''
    coll_product = Connect('product')
    result = aep_product_management.QueryProductList(appKey, appSecret, '', 1, 40)
    r = json.loads(result.decode('UTF-8'))
    rr = r['result']['list']
    for i in range(len(rr)):
        rr[i]['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(rr[i]['createTime'] / 1000))
        rr[i]['updateTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(rr[i]['updateTime'] / 1000))
        count = coll_product.count_documents({"productId": rr[i]["productId"]})
        if count == 0:
            coll_product.insert_one(rr[i])
        else:
            pass

def UpdateAllDevice(appKey:str, appSecret:str):
    '''
    更新数据库中所有产品下的设备
    '''
    coll_product = Connect('product')
    productId = []
    MasterKey = []
    for i in coll_product.find({}, {'_id': 0, 'productId': 1, 'apiKey': 1}):
        productId.append(i['productId'])
        MasterKey.append(i['apiKey'])
    for i in range(len(productId)):
        result = aep_device_management.QueryDeviceList(appKey, appSecret, MasterKey[i], productId[i], '', 1, 40)
        r = json.loads(result.decode('UTF-8'))
        rr = r['result']['list']
        coll_device = Connect('device')
        # 避免重复写入数据库
        for j in range(len(rr)):
            rr[j]['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(rr[j]['createTime'] / 1000))
            rr[j]['onlineAt'] = strftime('%Y/%m/%d %H:%M:%S', localtime(rr[j]['onlineAt'] / 1000))
            rr[j]['offlineAt'] = strftime('%Y/%m/%d %H:%M:%S', localtime(rr[j]['offlineAt'] / 1000))
            count = coll_device.count_documents({"deviceId": rr[j]["deviceId"]})
            if count == 0:
                coll_device.insert_one(rr[j])
            else:
                pass

def QueryProduct(productId:int, keywords:str):
    '''
    查询指定产品
    支持产品id和产品名关键词查询
    '''
    coll_product = Connect('product')
    r = list(coll_product.find({'$or': [{'productId': productId}, {'productName': {'$regex': keywords}}]}))
    if r == []:
        return "无结果"
    else:
        return r

def ProductList():
    '''
    产品列表
    '''
    coll_product = Connect('product')
    r = coll_product.find({},{'_id': 0, 'productId': 1, 'productName': 1, 'createTime': 1, 'deviceCount': 1, 'thirdTypeValue': 1})
    return r

def DeviceList():
    '''
    设备列表
    '''
    coll_device = Connect('device')
    r = coll_device.find({},{'_id': 0, 'deviceName': 1, 'deviceId':1, 'productId': 1, 'createTime': 1, 'onlineAt': 1, 'offlineAt': 1})
    # m = coll_device.aggregate([
    #     {
    #         '$lookup':
    #         {
    #             "from": "product",
    #             "localField": "productId",
    #             "foreignField": "productId",
    #             "as": "info"
    #         },
    #     },
    #     {
    #         '$project':
    #         {
    #             '_id': 0,
    #             'deviceName': 1,
    #             'productId': 1,
    #             'createTime': 1,
    #             'onlineAt': 1,
    #             'offlineAt': 1,
    #             'info.productName': 1,
    #         },
    #     }
    # ])
    return r

    
    






