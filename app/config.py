'''
相关配置参数
'''
class BaseConfig:
    '''
    通用配置
    '''
    DEBUG       = True # 允许调试，在正式平台上需要关闭
    SECRET_KEY  = 'this is a secret key!'   # session

Config = {
    'base': BaseConfig
}
