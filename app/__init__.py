from flask import Flask, Blueprint
from .config import DevelopmentConfig
from .resources import api
from .views import view
from flask_cors import CORS

# role based auth token 
# blueprint globally
# CORS
# Views/Controllers for time calc, Menu, INventory management


def create_app():

    # Flask app instance
    app = Flask(__name__)
    
    #Config
    app.config.from_object(DevelopmentConfig)
    

    api.init_app(app)

    app.register_blueprint(view, url_prefix="/")

    CORS(app)

    return app