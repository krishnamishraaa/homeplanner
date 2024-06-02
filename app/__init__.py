from flask import Flask
from .resources import api

# role based auth token 
# blueprint globally
# CORS
# Views/Controllers for time calc, Menu, INventory management


def create_app():

    # Flask app instance
    app = Flask(__name__)

    api.init_app(app)

    return app