'''
Database: Mongodb
涉及到数据库操作的函数
'''
from pymongo import MongoClient
from apis import aep_device_management
from apis import aep_product_management
from apis.aep_device_event import QueryEventList
from json import loads
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

def itemCount(item:str):
    collection = Connect(item)
    num = collection.find().count()
    return num

def UpdateAllProduct(appKey:str, appSecret:str):
    '''
    更新所有产品
    '''
    coll_product = Connect('product')
    result = aep_product_management.QueryProductList(appKey, appSecret, '', '', '')
    r = loads(result.decode('UTF-8'))
    rr = r['result']['list']
    # 删了重新添加
    coll_product.delete_many({})
    coll_product.insert(rr)
        

def UpdateAllDevice(appKey:str, appSecret:int):
    '''
    更新数据库中所有产品下的设备
    不能重复添加
    '''
    coll_product = Connect('product')
    coll_device = Connect('device')
    coll_device.delete_many({})
    productId = []
    MasterKey = []
    for i in coll_product.find({}, {'_id': 0, 'productId': 1, 'apiKey': 1}):
        productId.append(i['productId'])
        MasterKey.append(i['apiKey'])
    for i in range(len(productId)):
        result = aep_device_management.QueryDeviceList(appKey, appSecret, MasterKey[i], productId[i], '', '', '')
        r = loads(result.decode('UTF-8'))
        rr = r['result']['list']
        # 删了重加
        coll_device.insert(rr)

def UpdateEvent(appKey:str, appSecret:str):
    '''
    事件入库
    appKey,appSecret,MasterKey,productId,deviceId,eventType,startTime,endTime,PageNow,pageSize
    eventType --> 2-警报
    '''
    coll_product = Connect('product')
    coll_device = Connect('device')
    coll_event = Connect('event')
    r1 = coll_product.find({}, {'_id': 0, 'productId': 1, 'apiKey': 1})
    for j in r1:
        MasterKey = j['apiKey']
        productId = j['productId']
        r = coll_device.find({'productId': j['productId']}, {'_id': 0, 'deviceId': 1})
        for i in r:
            deviceId = i['deviceId']
            result = QueryEventList(appKey, appSecret, MasterKey, productId, deviceId, 2, '', '', 1, 40)
            r = loads(result.decode('UTF-8'))
            rr = r['result']['list']
            for k in rr:
                count = coll_event.count_documents({'createTime': k['createTime']})
                if count == 0:
                    coll_event.insert_many(rr)
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




