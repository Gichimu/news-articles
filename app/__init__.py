from flask import Flask

from flask_bootstrap import Bootstrap
from config import config_options
bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #setting up configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    #initializing flask extension
    bootstrap.init_app(app)


    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting up config
    from .requests import configure_request
    configure_request(app)
    

    # from app import views

    return app