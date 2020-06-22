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
from models import Connect
from models import itemCount
from models import UpdateAllDevice
from models import UpdateAllProduct
from models import UpdateEvent
from time import strftime, localtime




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
    coll_product = Connect('product')
    data = list(coll_product.find({}, {'_id': 0, 'productId': 1, 'productName': 1, 'createTime': 1, 'deviceCount': 1, 'thirdTypeValue': 1}))
    for i in data:
        i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
    return render_template('/product/product.html', products=data)


@app.route('/device/<int:productId>', methods=['GET'])
def device(productId):
    coll_device = Connect('device')
    data = list(coll_device.find({}, {'_id': 0, 'deviceName': 1, 'productId': 1, 'imei': 1, 'createTime': 1}))
    for i in data:
        i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
    return render_template('/product/device.html', devices = data)

@app.route('/device/newdevice')
def newdevice():
    return render_template('/product/new_device.html')

@app.route('/alarm')
def alarm():
    appKey = session.get('appKey')
    appSecret = session.get('appSecret')
    UpdateEvent(appKey, appSecret)
    coll_event = Connect('event')
    data = list(coll_event.find({'eventContent': {'$regex': '"smoke_state":1'}}, {'_id': 0, 'imei': 1, 'eventContent': 1, 'createTime': 1}))
    if not data:
        data = [{"imei": "暂无", "eventContent": "-", "createTime": "-"}]
    else:
        for i in data:
            i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
    return render_template('/product/alarm.html', events = data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

