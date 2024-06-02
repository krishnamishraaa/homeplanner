from flask_sqlalchemy import SQLAlchemy
from datetime import datetime , timedelta
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
# Create Flask app instance

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homeplanner.db'

# Create SQLAlchemy instance and bind it to the app
db = SQLAlchemy(app)

class User(db.Model): 
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String, unique= True, nullable= False)
    email = db.Column(db.String, unique=True)
    passwordhash = db.Column(db.String(255))
    name = db.Column(db.String)
    phone = db.Column(db.String(13))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.passwordhash = generate_password_hash(password)
    
    def checkpassword(self, password):
        return check_password_hash(self.passwordhash, password)


# Define SQLAlchemy models
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(13))
    role = db.Column(db.String(50))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    frequency = db.Column(db.String(20))
    assigned_to = db.Column(db.Integer, db.ForeignKey('member.id'))
    day_of_week = db.Column(db.String(20))
    priority = db.Column(db.Integer)

    member = db.relationship('Member', backref='tasks')

class WeekendTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    day_of_week = db.Column(db.String(20))

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(20))
    breakfast = db.Column(db.Text)
    lunch = db.Column(db.Text)
    supper = db.Column(db.Text)
    dinner = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    inventory_codes = db.Column(db.Text)

class ShoppingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    quantity = db.Column(db.String(20))
    unit = db.Column(db.String(20))
    inventory_code = db.Column(db.String(20))
    category = db.Column(db.String(20))
    member = db.Column(db.Integer, db.ForeignKey('member.id'))
    member = db.relationship('Member', backref='shopping_list')

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    quantity = db.Column(db.String(20))
    unit = db.Column(db.String(20))
    inventory_code = db.Column(db.String(20))
    category = db.Column(db.String(20))
    member = db.Column(db.Integer, db.ForeignKey('member.id'))
    member = db.relationship('Member', backref='inventory')
