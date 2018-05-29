
from peewee import *

class Config:
    HOST = '0.0.0.0' # this is not registering
    PORT = 8000 # this is not registering
    SECRET_KEY = 'GWK~M$F2"|[|i|,KEJWxvA5~JQN!}fUz>|&h`>g.K2/p)%t3%4P:tuR6G6A'
    DEFAULT_RATE = ["1000/hour"]
    TODO_LIMITS = "100/hour"
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = SqliteDatabase('todo_dev.db')
    

class TestingConfig(Config):
    TESTING = True
    DATABASE = SqliteDatabase(':memory:')


class ProductionConfig(Config):
    pass    


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}