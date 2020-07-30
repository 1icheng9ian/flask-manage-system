# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/27
'''

from app import db


PROTOCOL = {1: 'T-LINK协议', 2: 'MQTT协议', 3: 'LWM2M协议',
            4: 'TUP协议', 5: 'HTTP协议', 6: 'JT/T808',
            7: 'TCP协议', 8: '私有TCP网关子设备协议',
            9: '私有UDP网关子设备协议', 10: '网关产品MQTT网关产品协议',
            11: '南向云'}

class PublicProduct(db.Document):
    productId = db.StringField(required=True)
    productName = db.StringField(max_length=255)
    tupDeviceModel = db.StringField()
    apiKey = db.StringField()
    productProtocol = db.StringField()
    productTypeValue = db.StringField()
    secondaryTypeValue = db.StringField
    thirdTypeValue = db.StringField()