from flask import Flask, render_template, request, redirect ,url_for, session, jsonify
from exts import CheckAccess
from model import saveaccout, ProductList, DeviceList, UpdateAllDevice, UpdateAllProduct, itemCount
from config import config

app = Flask(__name__)
# 导入配置
app.config.from_object(config['base'])

# index页
@app.route('/')
def index():
    return render_template('index.html')

# 主页
@app.route('/home')
def home():
    return render_template('home.html')

# 产品页
@app.route('/product/')
def product():
    return render_template('/product/product.html')

# 设备页
@app.route('/device/')
def device():
    return render_template('/product/device.html')

# 警报信息
@app.route('/alarm/')
def alarm():
    return render_template('/product/alarm.html')

# 登录页
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        appKey      = request.form.get('username')
        appSecret   = request.form.get('password', type=str, default=None)
        message = CheckAccess(appKey, appSecret)    # 验证账号
        saveaccout(appKey, appSecret)
        if '成功' in message:
            session['appKey'] = appKey
            session['appSecret'] = appSecret
            session.permanent = True
            return redirect(url_for('product'))
        else:
            return render_template('login.html')


# 保持登录状态
@app.context_processor
def my_context_processor():
    user = session.get('appKey')
    if user:
        return { 'login_user': user }
    return {}

# 注销
@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))
    
# 刷新数字
@app.context_processor
def refreshproduct():
    appKey = session.get('appKey')
    appSecret = session.get('appSecret')
    product_count = UpdateAllProduct(appKey, appSecret)
    return {'productCount': product_count}
@app.context_processor
def refreshdevice():
    appKey = session.get('appKey')
    appSecret = session.get('appSecret')
    device_count = UpdateAllDevice(appKey, appSecret)
    return {'deviceCount': device_count}

# 查询数据库信息，显示在表格
@app.route('/query_product', methods=['GET', 'POST'])
def query_product():
    count = itemCount('product')
    product_data = ProductList()
    table_result = {"code": 0,
    "msg": None,
    "count": count,
    "data": list(product_data)}
    return jsonify(table_result)
@app.route('/query_device', methods=['GET', 'POST'])
def query_device():
    count = itemCount('device')
    device_data = DeviceList()
    table_result = {"code": 0,
    "msg": None,
    "count": count,
    "data": list(device_data)}
    return jsonify(table_result)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
