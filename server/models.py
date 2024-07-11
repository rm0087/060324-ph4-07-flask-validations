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

    @validates('username')
    def validate_username(self, key, value):
        user = User.query.where(User.username == value).first()
        if value and len(value.strip().replace(' ', '_')) < 4:
            raise ValueError('Username must be greater than or equal to 4 characters')
        if user:
            raise ValueError('Username must be unique!')
        return value.strip().replace(' ', '_')
    

    @validates('email')
    def validate_email(self, key, value):
        if '$' in value:
            raise ValueError(f'Invalid characters for {key}!')
        return value
    

    @validates('age')
    def validate_age(self, key, value):
        if value >= 13:
            return value
        else:
            raise ValueError('Must be at least 13 years old!')