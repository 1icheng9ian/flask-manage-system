'''
Database: Mongodb
'''
from pymongo import MongoClient
from werkzeug.security import generate_password_hash #加密
host = '127.0.0.1'
port = 27017
dbname = 'NBdatabase'


def saveaccout(appKey:str, appSecret:str):
    '''
    保存账号到数据库
    密码加密
    '''
    # 连接 mongodb
    connect = MongoClient(host, port)
    db = connect.NBdatabase
    account = db.usr
    r = account.find_one({'appkey': appKey})
    if r == None:
        appsecret_m = generate_password_hash(appSecret)
        account.insert_one({'appkey': appKey, 'appSecret': appsecret_m})
    else:
        pass

def SaveManyData(clname:str, data:dict):
    '''
    连接 mongodb
    数据库名和collection名
    '''
    connect = MongoClient(host, port)
    db = connect[dbname]
    collection = db[clname]
    collection.insert_many(data)

