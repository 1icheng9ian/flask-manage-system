'''
相关配置参数
'''
class BaseConfig:
    '''
    通用配置
    '''
    DEBUG       = True # 调试
    SECRET_KEY  = 'this is a secret key!'   # session

Config = {
    'base': BaseConfig
}
