from turtle import title
from . import db
from datetime import datetime

class Restaurant(db.Model):
    """data model from restuarant"""
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True, index=False)
    email = db.Column(db.String(255), nullable=False, unique=True, index=False)
    menus = db.relationship('Menu', backref='restaurant', cascade='all, delete, delete-orphan', single_parent=True, order_by='desc(Menu.title)')
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

class Menu(db.Model):
    """data model for restuarant menu"""
    __tablename__='menu'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)