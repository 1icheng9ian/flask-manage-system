# -*- encoding: utf-8 -*-
'''
@Time    :   2020/07/04
'''

import datetime

from flask import (current_app, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from flask_principal import AnonymousIdentity, Identity, identity_changed

from . import models
from .forms import LoginForm, ModifyPasswordForm, RegisterForm, UpdateProfileForm


def login():
    '''
    普通用户登录
    '''
    if current_user.is_authenticated and current_user.role == 'admin':
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        try:
            # 从数据库中查找username
            user = models.User.objects.get(username=form.username.data)
        except models.User.DoesNotExist:
            # 没有注册过，就是None
            user = None
        if user.role == 'admin':
            if user and user.verify_password(form.password.data):
                # 如果注册过，并且密码验证通过
                # 修改最后登录时间
                login_user(user)
                user.last_login_time = datetime.datetime.now
                user.save()
                identity_changed.send(current_app._get_current_object(), identity=Identity(user.username))
                return redirect(url_for('main.index'))
            flash('用户名或密码错误', 'danger')
        else:
            flash('该账号为超级管理员账号，请从超级管理员入口登录！', 'warning')

    return render_template('accounts/login.html', form=form)

def register():
    # 创建表单对象
    form = RegisterForm()

    # 判断form中的数据是否合理
    if form.validate_on_submit():
        # 验证合格，提取数据
        user = models.User()
        super_user = models.User()
        user.username = form.username.data
        user.password = form.password.data
        user.role = form.role.data
        if models.User.objects.filter(role='super_admin').count() > 0 and user.role == 'super_admin':
            flash('当前不可注册超级账户', 'warning')
            
        else:
            user.save()
            flash('注册成功', 'success')
            return redirect(url_for('accounts.login'))

    return render_template('accounts/register.html', form=form)

@login_required     # 需要登录才能的操作，需要 login_required
def logout():
    logout_user()
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    identity_changed.send(current_user._get_current_object(), identity=AnonymousIdentity())
    flash('已退出', 'success')
    return redirect(url_for('accounts.login'))

@login_required
def user():
    return render_template('accounts/user.html')

@login_required
def update_profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        user = current_user
        user.cellphone = form.cellphone.data
        user.company = form.company.data
        user.address = form.address.data
        user.save()
        # 修改完成后跳转到查看界面
        return redirect(url_for('accounts.user'))
    return render_template('accounts/update_profile.html', form=form)

@login_required
def update_pass():
    form = ModifyPasswordForm()
    if form.validate_on_submit():
        user = current_user
        if form.current_password.data != form.confirm_password.data:
            user.password = form.confirm_password.data
            user.save()
            return redirect(url_for('main.index'))
        flash('新密码和原密码一样，请重输！', 'danger')
    return render_template('accounts/update_pass.html', form=form)
