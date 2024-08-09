from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from config import db
from datetime import datetime

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

    

    @validates('year_joined')
    def validate_year_joined(self,key, value):

        current_year = datetime.now().year

        if not type(value) == int:
            raise ValueError('year_joined must be an integer')
        if value not in range(2000, current_year + 1):
            raise ValueError(f'year_joined must be between 2000 and {current_year}')
        return value

    @validates('email')
    def validate_email(self,key,value):
        if value.count('@') != 1:
            raise ValueError('Invalid email format')
        return value.lower()

    @validates('username')
    def validate_naughty(self, key, value):
        naughty_words = ['heck', 'bish', 'frack']
        for word in naughty_words:
            if word in value:
                raise ValueError('Naughty word!')
        return value

    @validates('phone_number')
    def validate_phone(self, key, value):
        val_number = value.replace('-', '')
        
        if len(val_number) != 10:
            raise ValueError('Must be a valid 10 digit phone number')
        return val_number
    
    @validates('address')
    def validate_address(self, key,value):
        street_types = ['Street', 'Avenue', 'Road']
        valid_nos = (1234567890)
        zip_check = value[slice(-5, len(value), 1)]
        
        if zip_check in valid_nos:
            for word in street_types:
                if word in value:
                    return value
        else:
            raise ValueError('Must end with a 5 digit zip-code')
        raise ValueError('Must be a Road, Street, or Avenue')

