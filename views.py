'''
路由
'''
from config import Config
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask import jsonify
from models import itemCount
from models import ProductList
from models import DeviceList
from models import EventList
from models import UpdateAllDevice
from models import UpdateAllProduct
from models import UpdateEvent
from json import loads
from time import localtime
from time import strftime
from apis.aep_device_management import DeleteDevice



app = Flask(__name__)
app.config.from_object(Config['base'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        appKey = request.form.get('username')
        appSecret = request.form.get('password', type=str, default=None)
        session['appKey'] = appKey
        session['appSecret'] = appSecret
        session.permanent = True
        return redirect(url_for('home'))

@app.context_processor
def keeplog():
    user = session.get('appKey')
    if user:
        return { 'login_user': user }
    return {}
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/update')
def update():
    appKey = session.get('appKey')
    appSecret = session.get('appSecret')
    UpdateAllProduct(appKey, appSecret)
    UpdateAllDevice(appKey, appSecret)
    return redirect(url_for('home'))


@app.context_processor
def refresh():
    product_count = itemCount('product')
    device_count = itemCount('device')
    return {'productCount': product_count, 'deviceCount': device_count}

@app.route('/product')
def product():
    return render_template('/product/product.html')

@app.route('/query_product', methods=['GET', 'POST'])
def query_product():
    count = itemCount('product')
    data = ProductList()
    data_list = []
    for i in data:
        i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
        data_list.append(i)
    table_result = {"code": 0,
    "msg": "",
    "count": count,
    "data": data_list}
    return jsonify(table_result)

@app.route('/event')
def event():
    return render_template('/product/event.html')

@app.route('/update_event')
def update_event():
    appKey = session.get('appKey')
    appSecret = session.get('appSecret')
    UpdateEvent(appKey,appSecret)
    return redirect(url_for('event'))
    
# 此页面只能显示对应的上报事件
# 通过deviceId来区分
@app.route('/query_event', methods=['GET', 'POST'])
def query_event():
    count = itemCount('event')
    data = EventList()
    data_list = []
    for i in data:
        i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
        data_list.append(i)
    table_result = {"code": 0,
    "msg": "",
    "count": count,
    "data": data_list}
    return jsonify(table_result)

@app.route('/query_device', methods=['GET', 'POST'])
def query_device():
    count = itemCount('device')
    data = DeviceList()
    data_list = []
    for i in data:
        i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
        if i['onlineAt']:
            i['onlineAt'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['onlineAt'] / 1000))
        else:
            i['onlineAt'] = '-'
        if i['updateTime']:
            i['updateTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['updateTime'] / 1000))
        else:
            i['updateTime'] = '-'
        data_list.append(i)
    table_result = {"code": 0,
    "msg": "",
    "count": count,
    "data": data_list}
    return jsonify(table_result)

@app.route('/device')
def device():
    return render_template('/product/device.html')

# @app.route('/delete')
# def delete():
    # appKey = session.get('appKey')
    # appSecret = session.get('appSecret')
    # MasterKey = 
    # productId = 
    # data = request.form.get('data')
    # DeleteDevice(appKey, appSecret, MasterKey, productId, deviceIds)
    # # 数据库同步也要删除
    

@app.route('/alarm')
def alarm():
    return render_template('/product/alarm.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

