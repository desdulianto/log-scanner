import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('LOG_SCANNER_SECRET_KEY')
    UPLOADED_LOGS_DEST = '/tmp'
    UPLOADED_LOGS_ALLOW = ('zip', 'log')

class Development(Config):
    DEBUG = True


class Testing(Config):
    Testing = True


class Production(Config):
    pass
