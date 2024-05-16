#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"



# USER ROUTES ################################


@app.get('/users')
def all_users():
    return [u.to_dict() for u in User.query.all()], 200


@app.get('/users/<int:id>')
def user_by_id(id):
    user = User.query.where(User.id == id).first()
    if user:
        return user.to_dict(), 200
    else:
        return {'error': 'Not found'}, 404
    

@app.post('/users')
def post_user():
    user = User(
        username=request.json.get('username'),
        email=request.json.get('email'),
        address=request.json.get('address'),
        phone_number=request.json.get('phone_number'),
        age=request.json.get('age'),
        vip=request.json.get('vip')
    )
    db.session.add(user)
    db.session.commit()
    return user.to_dict(), 201


@app.patch('/users/<int:id>')
def patch_user_by_id(id):
    user = User.query.where(User.id == id).first()
    if user:
        for key in request.json.keys():
            setattr(user, key, request.json[key])
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 202
    else:
        return {'error': 'Not found'}, 404
    

@app.delete('/users/<int:id>')
def delete_user_by_id(id):
    user = User.query.where(User.id == id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return {}, 204
    else:
        return {'error': 'Not found'}, 404


# RUN ##########################

if __name__ == '__main__':
    app.run(port=5555, debug=True)