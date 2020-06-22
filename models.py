'''
Database: Mongodb
'''
from pymongo import MongoClient
from apis.aep_device_management import QueryDeviceList
from apis.aep_product_management import QueryProductList
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
    num = collection.count_documents({})
    return num

def UpdateAllProduct(appKey:str, appSecret:str):
    '''
    更新所有产品
    考虑到直接在电信平台直接操作增删的情况
    简单粗暴, 将原有的数据全删了，重新放入
    '''
    coll_product = Connect('product')
    result = QueryProductList(appKey, appSecret, '', '', '')
    r = loads(result.decode('UTF-8'))
    rr = r['result']['list']
    coll_product.delete_many({})
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
    coll_device = Connect('device')
    productId = []
    MasterKey = []
    coll_device.delete_many({})
    for i in coll_product.find({}, {'_id': 0, 'productId': 1, 'apiKey': 1}):
        productId.append(i['productId'])
        MasterKey.append(i['apiKey'])
    for i in range(len(productId)):
        result = QueryDeviceList(appKey, appSecret, MasterKey[i], productId[i], '', '', '')
        r = loads(result.decode('UTF-8'))
        rr = r['result']['list']
        # 避免重复写入数据库
        for j in rr:
            count = coll_device.count_documents({"deviceId": j["deviceId"]})
            if count == 0:
                coll_device.insert_one(j)
            else:
                pass


def UpdateEvent(appKey:str, appSecret:str):
    '''
    事件入库
    appKey,appSecret,MasterKey,productId,deviceId,eventType,startTime,endTime,PageNow,pageSize
    eventType --> 2-警报
    '''
    coll_product = Connect('product')
    coll_device = Connect('device')
    coll_event = Connect('event')
    coll_event.delete_many({})
    r1 = coll_product.find({}, {'_id': 0, 'productId': 1, 'apiKey': 1})
    for j in r1:
        MasterKey = j['apiKey']
        productId = j['productId']
        r = coll_device.find({'productId': j['productId']}, {'_id': 0, 'deviceId': 1})
        for i in r:
            deviceId = i['deviceId']
            result = QueryEventList(appKey, appSecret, MasterKey, productId, deviceId, 2, '', '', '', '')
            r = loads(result.decode('UTF-8'))
            rr = r['result']['list']
            for k in rr:
                count = coll_event.count_documents({'createTime': k['createTime']})
                if count == 0:
                    coll_event.insert_many(rr)
                else:
                    pass


