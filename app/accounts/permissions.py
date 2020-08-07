# -*- encoding: utf-8 -*-
'''
@Time    :   2020/08/05
'''

from flask_principal import RoleNeed, Permission, identity_loaded, UserNeed
from flask_login import current_user

super_admin_need = RoleNeed('super_admin')
admin_need = RoleNeed('admin')

super_admin_Permission = Permission(super_admin_need)
admin_Permission = Permission(admin_need).union(super_admin_Permission)

@identity_loaded.connect
def on_identity_change(sender, identity):
    identity.user = current_user

    # 判断对象是否有'username'属性
    if hasattr(current_user, 'username'):
        identity.provides.add(UserNeed(current_user.username))

    if hasattr(current_user, 'role'):
        identity.provides.add(RoleNeed(current_user.role))

    if hasattr(current_user, 'is_superuser') and current_user.is_superuser:
        identity.provides.add(super_admin_need)

    # allows 方法：允许该role拥有此权限
    identity.allow_super_admin = super_admin_Permission.allows(identity)
    identity.allow_admin = admin_Permission.allows(identity)
