from flask import Blueprint

view = Blueprint('views', __name__)


@view.get('/')
def home():
    return "Hello World!!"
