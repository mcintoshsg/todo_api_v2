''' app cofig '''
import os


class Config:
    HOST = '0.0.0.0'
    PORT = 8000
    SECRET_KEY = 'GWK~M$F2"|[|i|,KEJWxvA5~JQN!}fUz>|&h`>g.K2/p)%t3%4P:tuR6G6A'
    DEFAULT_RATE = "100/hour"

    @staticmethod
    def init_app(app):
        pass    

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #     'sqlite://'


# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    
    'default': DevelopmentConfig
}
    