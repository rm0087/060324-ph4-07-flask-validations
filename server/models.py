from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db

# USER MODEL

class User(db.Model, SerializerMixin):
    
    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    address = db.Column(db.String)
    phone_number = db.Column(db.String)
    age = db.Column(db.Integer)
    vip = db.Column(db.Boolean)
    year_joined = db.Column(db.Integer)