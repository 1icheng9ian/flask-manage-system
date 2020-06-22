'''
Database: Mongodb
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
    result = aep_product_management.QueryProductList(appKey, appSecret, '', 1, 40)
    r = loads(result.decode('UTF-8'))
    rr = r['result']['list']
    for i in rr:
        count = coll_product.count_documents({"productId": i["productId"]})
        if count == 0:
            coll_product.insert_one(i)
        else:
            pass

def UpdateAllDevice(appKey:str, appSecret:int):
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
        r = loads(result.decode('UTF-8'))
        rr = r['result']['list']
        coll_device = Connect('device')
        # 避免重复写入数据库
        for j in rr:
            count = coll_device.count_documents({"deviceId": j["deviceId"]})
            if count == 0:
                coll_device.insert_one(j)
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
    r = coll_device.find({},{'_id': 0, 'deviceName': 1, 'deviceId':1, 'productId': 1, 'createTime': 1, 'onlineAt': 1, 'updateTime': 1})
    return r

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

def EventList():
    coll_event = Connect('event')
    r = coll_event.find({},{'_id': 0, 'eventContent': 1, 'createTime': 1})
    return r


def RemoveDevice(deviceId:str):
    '''
    根据设备id删除设备
    '''
    coll_device = Connect('device')
    coll_device.delete_one({'deviceId': deviceId})

def RemoveProduct(productId:int):
    '''
    删除产品，前提是该产品下无设备
    '''
    coll_product = Connect('product')
    coll_product.delete_one({'productId': productId})
