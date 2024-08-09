#!/usr/bin/env python3

from flask import request
from config import app, db
from models import db, User

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
    try:
        user = User(
            username=request.json.get('username'),
            email=request.json.get('email'),
            address=request.json.get('address'),
            phone_number=request.json.get('phone_number'),
            age=request.json.get('age'),
            vip=request.json.get('vip'),
            year_joined=request.json.get('year_joined')
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 201
    except sqlalchemy.exc.IntegrityError as error:
        return { 'error': 'Invalid data' }, 400
    except ValueError as error:
        return { 'error': str(error) }, 400


@app.patch('/users/<int:id>')
def patch_user_by_id(id):
    user = User.query.where(User.id == id).first()
    if user:
        try:
            for key in request.json:
                setattr(user, key, request.json[key])
            db.session.add(user)
            db.session.commit()
            return user.to_dict(), 202
        except:
            return { 'error': 'Invalid data' }, 400
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