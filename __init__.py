from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr

from todo_api_v2.config import config

limiter = Limiter()    

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # limiter.init_app(app)
    # limiter = Limiter(global_limits=[config.DEFAULT_RATE], key_func=get_ipaddr)
    # limiter.limit("40/day")(users_api)
    # limiter.limit(config.DEFAULT_RATE, per_method=True, 
    #           methods=['post', 'put', 'delete'])(todos_api)
   
    from todo_api_v2.resources.tasks import todos_api
    from todo_api_v2.resources.users import users_api
    from todo_api_v2.main.routes import main

    app.register_blueprint(main)
    app.register_blueprint(todos_api, url_prefix='/api/v1')
    app.register_blueprint(users_api, url_prefix='/api/v1')
    
    return app