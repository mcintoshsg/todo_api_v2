from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr

from peewee import *

from config import config


limiter = Limiter()    
db_proxy = Proxy()

def create_app(config_name):
    app = Flask(__name__)
    # pdb.set_trace()
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # limiter.init_app(app)
    
    db_proxy.initialize(config[config_name].DATABASE)
    # DATABASE.create_tables([User, Todo], safe=True)
    # DATABASE.close()
    
    from todo.resources.tasks import todos_api
    from todo.resources.users import users_api
    from todo.main.routes import main

    app.register_blueprint(main)
    app.register_blueprint(todos_api, url_prefix='/api/v1')
    app.register_blueprint(users_api, url_prefix='/api/v1')
    
    # limiter = Limiter(global_limits=config[config_name].DEFAULT_RATE, key_func=get_ipaddr)
    # limiter.limit("40/day")(users_api)
    # limiter.limit(config[config_name].DEFAULT_RATE, per_method=True, 
    #            methods=['post', 'put', 'delete'])(todos_api)

    return app