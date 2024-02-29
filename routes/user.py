import hashlib
from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from models.user import db, User
user_api = Blueprint('user_api',__name__)

@user_api.route('/login_user',methods=['POST'])
def login_user():
    try:
        data = request.json
        username = data['username']
        password = hashlib.sha256((data['password']).encode()).hexdigest()
        user = User.query.filter_by(username=username,password=password).first()
        if user is None:
            return jsonify({'message':'Invalid credentials'}),401
        return jsonify({'message':'Login successful'}),200
    except Exception as e:
        return jsonify({'message':f'Error {e}'}),500
    
@user_api.route('/create_user',methods=['POST'])
def create_user():
    try:
        data = request.json
        username = data['username']
        password = hashlib.sha256((data['password']).encode()).hexdigest()
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message':f'Error {e}'}),500