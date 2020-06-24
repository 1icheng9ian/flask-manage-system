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
# config.py 中的 debug 模式在正式平台上需要关闭
app.config.from_object(Config['base'])

@app.route('/')
def index():
    '''
    导航页；有几张图片在这里轮播
    '''
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        appKey = request.form.get('username')
        appSecret = request.form.get('password', type=str, default=None)
        # session 存储 appKey 和 appSecret 后续可以继续使用
        session['appKey'] = appKey
        session['appSecret'] = appSecret
        session.permanent = True
        return redirect(url_for('home'))

# 上下文处理器：
# 返回的结果可以作为全局可访问的变量
@app.context_processor
def keeplog():
    user = session.get('appKey')
    if user:
        return { 'login_user': user }
    return {}
    

@app.route('/logout')
def logout():
    '''
    点击注销后要清除 session
    '''
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
    # 显示设备数量和产品数量
    product_count = itemCount('product')
    device_count = itemCount('device')
    return {'productCount': product_count, 'deviceCount': device_count}

@app.route('/product')
def product():
    coll_product = Connect('product')
    data = list(coll_product.find({}, {'_id': 0, 'productId': 1, 'productName': 1, 'createTime': 1, 'deviceCount': 1, 'thirdTypeValue': 1}))
    # data 的类型是 mongo cursor (游标)
    # cursor 不是查询结果，而是查询返回的接口，通过它可以逐条读取
    # 将时间戳转为本地时间
    for i in data:
        i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
    # 返回的路由页面，这个页面需要返回数据
    return render_template('/product/product.html', products=data)

# < > 中是动态路由
# int 限制了 productId 的类型
@app.route('/device/<int:productId>', methods=['GET'])
def device(productId):
    coll_device = Connect('device')
    data = list(coll_device.find({}, {'_id': 0, 'deviceName': 1, 'productId': 1, 'imei': 1, 'createTime': 1}))
    for i in data:
        i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
    return render_template('/product/device.html', devices = data)

@app.route('/device/newdevice')
def newdevice():
    '''
    创建新的设备
    '''
    return render_template('/product/new_device.html')

@app.route('/alarm')
def alarm():
    appKey = session.get('appKey')
    appSecret = session.get('appSecret')
    # UpdateEvent(appKey, appSecret)
    coll_event = Connect('event')
    # 匹配查询
    # 后续：
    # 添加一个选项，可以选择消息类型
    data = list(coll_event.find({'eventContent': {'$regex': '"smoke_state":1'}}, {'_id': 0, 'imei': 1, 'eventContent': 1, 'createTime': 1}))
    # 出现结果为空，需要填充一个空值的返回值
    if not data:
        data = [{"imei": "暂无", "eventContent": "-", "createTime": "-"}]
    else:
        for i in data:
            i['createTime'] = strftime('%Y/%m/%d %H:%M:%S', localtime(i['createTime'] / 1000))
    return render_template('/product/alarm.html', events = data)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

