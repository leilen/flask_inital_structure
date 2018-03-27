class Config(object):
    DEBUG = True
    TESTING = False
    SEND_FILE_MAX_AGE_DEFAULT = 0

class DevelopmentConfig(Config):
    pass

config = {
    'dev' : DevelopmentConfig,
    'pro' : DevelopmentConfig
}