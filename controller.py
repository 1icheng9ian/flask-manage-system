'''
附加函数
'''
# from apis.aep_device_management import CreateDevice
from apis.aep_device_status import QueryDeviceStatusList
from models import Connect
from json import loads, dumps

# def create_device(appKey: str, appSecret:str, MasterKey:str, name: str, imei: str, operator: str, autosub: int, productId: int):
#     coll_device = Connect('device')
#     devices = coll_device.find_one({'imei': imei})
#     if devices:
#         return '设备已存在'
#     else:
#         body_dict = {
#             'deviceName': name,
#             'imei': imei,
#             'operator': operator,
#             'other':{
#                 'autoObserver': autosub,
#                 'imsi': '',
#                 'pskValue': ''
#                 },
#                 'productId': productId
#                 }
#         body = dumps(body_dict)
#         result = CreateDevice(appKey, appSecret, MasterKey, body)
#         r = loads(result.decode('UTF-8'))
#         return r['msg']

def Device_new_status(appKey:str, appSecret:str, productId: int, deviceId: str):
    body_dict = {
        'productId': productId,
        'deviceId': deviceId,
    }
    body = dumps(body_dict)
    result = QueryDeviceStatusList(appKey, appSecret, body)
    r = loads(result.decode('UTF-8'))
    return r['deviceStatusList']

# productId = 10064766
# deviceId = '7ebb7fd5529449dc8b6fda50d2bb75b9'
# appKey = 'xUK4gwn5EEa'
# appSecret = 'dbn9H64scs'

# r = Device_new_status(appKey,appSecret,productId,deviceId)
# print(len(r))
