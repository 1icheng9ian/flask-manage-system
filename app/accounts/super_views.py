# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/24
'''
from flask import render_template, redirect, url_for, flash, current_app, request
from flask_login import current_user, login_user, login_required
from flask_principal import identity_changed, Identity
from .super_forms import EditAdminInfoForm, AddPublicProductForm, EditBulletinForm
from .forms import SuperLoginForm
from . import models
from . import super_models
from .super_models import PROTOCOL
import datetime
from apis.aep_product_management import QueryProduct, DeleteProduct
from json import loads


def login():
    '''
    超级用户登录界面
    '''
    form = SuperLoginForm()
    # 验证输入的信息
    if form.validate_on_submit():
        try:
            user = models.User.objects.get(username=form.username.data)
        except models.User.DoesNotExist:
            user = None
        if user.role == 'super_admin':
            if user and user.verify_password(form.password.data):
                login_user(user)
                user.last_login_time = datetime.datetime.now
                user.save()
                identity_changed.send(current_app._get_current_object(), identity=Identity(user.username))
                return redirect(url_for('super_admin.index'))
            flash('用户名或密码错误', 'danger')
        else:
            flash('该账号为普通账号，请从普通管理员入口登录！', 'warning')

    return render_template('super_admin/login.html', form=form)

@login_required
def super_user():
    return render_template('super_admin/super_user.html')

@login_required
def super_user_edit():
    form = EditAdminInfoForm()
    if form.validate_on_submit():
        user = current_user
        user.appkey = form.appkey.data
        user.appsecret = form.appsecret.data
        user.save()
        return redirect(url_for('super_admin.super_user'))
    return render_template('super_admin/super_user_edit.html', form=form)

@login_required
def index():
    '''
    index 显示管理的各个项目
    暂时先就显示用户组
    '''
    users = models.User.objects.filter(role='admin')

    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    
    users = users.paginate(page=cur_page, per_page=10)

    data = {'users': users}
    return render_template('super_admin/index.html', **data)

@login_required
def product_management():
    '''
    添加公司的产品public product，之后其他用户可以直接选取
    普通用户不需要知道productId
    直接输入imei就完事了
    '''
    form = AddPublicProductForm()

    if form.validate_on_submit():
        public_product = super_models.PublicProduct()
        productId = form.productId.data
        # acquire current user infomation
        user = current_user
        if not user.appkey:
            flash('出错了！请先添加appkey和appsecret!', 'warning')
        else:
            appkey = user.appkey
            appsecret = user.appsecret
            public_product.productId = form.productId.data
            # aep平台验证
            result = QueryProduct(appKey=appkey, appSecret=appsecret, productId=productId)
            result = loads(result.decode('UTF-8'))
            # 需要考虑到用户输错的情况
            if result['code'] == 0:
                public_product.productName = result['result']['productName']
                public_product.tupDeviceModel = result['result']['tupDeviceModel']
                public_product.apiKey = result['result']['apiKey']
                public_product.productProtocol = PROTOCOL[result['result']['productProtocol']] # 数字对应的协议
                public_product.productTypeValue = result['result']['productTypeValue']
                public_product.secondaryTypeValue = result['result']['secondaryTypeValue']
                public_product.thirdTypeValue = result['result']['thirdTypeValue']
                public_product.save()   # 保存
                flash('添加成功', 'success')
                return redirect(url_for('super_admin.product_management'))
            else:
                flash(result['msg'], 'warning') # 使用aep平台的error message
    # acquire data
    public_products = super_models.PublicProduct.objects.all()
    data = {'public_products': public_products}
    return render_template('super_admin/product_management.html', form=form, **data)

@login_required
def delete_public_product(productId):
    # 危险操作
    # 这里进行删除操作的时候加上询问框
    # 删除只需要从数据库中删除，aep平台不需要
    # 如果下面有产品，不能删除
    # 这里查询device count的方法是向aep平台发送一条查询指令
    # 这可能会带来一些问题，如直接在平台添加的设备，会查找不到
    # 如后期aep平台按查询次数收费，可以酌情修改
    this_product = super_models.PublicProduct.objects.get_or_404(productId=productId)
    user = current_user
    appkey = user.appkey
    appsecret = user.appsecret
    result = QueryProduct(appKey=appkey, appSecret=appsecret, productId=productId)
    result = loads(result.decode('UTF-8'))
    if result['result']['deviceCount'] == 0:
        this_product.delete()
    else:
        flash('该产品下还有设备, 禁止删除!', 'danger')
    return redirect(url_for('super_admin.product_management'))

@login_required
def create_public_product():
    # 该功能暂时不可用
    # 通过aep平台直接创建产品
    return render_template('super_admin/create_public_product.html')

@login_required
def history():
    histories = super_models.History.objects.all()

    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1

    histories = histories.paginate(page=cur_page, per_page=10)

    data = {'histories': histories}
    return render_template('super_admin/history.html', **data)

@login_required
def super_bulletin():
    notices = super_models.Bulletin.objects.all()
    try:
        cur_page = int(request.args.get('page', 1))
    except:
        cur_page = 1
    notices = notices.paginate(page=cur_page, per_page=5)
    data = {'notices': notices}
    return render_template('super_admin/super_bulletin.html', **data)

@login_required
def edit_bulletin():
    form = EditBulletinForm()
    if form.validate_on_submit():
        board = super_models.Bulletin()
        board.title = form.title.data
        board.content = form.content.data
        board.author = current_user.username
        board.save()
        return redirect(url_for('super_admin.super_bulletin'))
    return render_template('super_admin/edit_bulletin.html', form=form)