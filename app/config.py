import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('LOG_SCANNER_SECRET_KEY')


class Development(Config):
    DEBUG = True


class Testing(Config):
    Testing = True


class Production(Config):
    pass
