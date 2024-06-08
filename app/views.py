from flask import Blueprint, render_template

view = Blueprint('views', __name__)


@view.get('/')
def home():
    return render_template('dashboard.html')

