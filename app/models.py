from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) , nullable = False)
    description = db.Column(db.String(150) , nullable = False)
    ingredients = db.Column(db.String(500), nullable = False)
    frequency = db.Column(db.Integer, nullable = False)
    

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) , nullable = False)
    quantity = db.Column(db.Float, nullable = False)
    consumed = db.Column(db.Float, nullable = False)
    unit = db.Column(db.String(20), nullable = False)
    

