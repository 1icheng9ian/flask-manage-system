from flask import Flask, render_template, request, redirect ,url_for, session
from exts import CheckAccess
from model import saveaccout, ProductList, DeviceList
from config import config

app = Flask(__name__)
# 导入配置
app.config.from_object(config['base'])

# 首页 
@app.route('/')
def home():
    return render_template('home.html')

# 产品页
@app.route('/product/')
def product():
    products = ProductList()
    return render_template('/product/product.html', products=products)

# 设备页
@app.route('/device/')
def device():
    devices = DeviceList()
    return render_template('/product/device.html', devices=devices)


# 登录页
@app.route('/access/', methods=['GET', 'POST'])
def access():
    if request.method == 'GET':
        return render_template('access.html')
    else:
        appKey      = request.form.get('appKey')
        appSecret   = request.form.get('appSecret', type=str, default=None)
        message = CheckAccess(appKey, appSecret)    # 验证账号
        saveaccout(appKey, appSecret)
        if '成功' in message:
            session['appKey'] = appKey
            session.permanent = True
            return redirect(url_for('product'))
        else:
            return render_template('access.html')


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
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
