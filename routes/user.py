import datetime
import hashlib
import jwt
from flask import Blueprint, request, jsonify
from models.model import db, User
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
        token = jwt.encode({'username':user.username,
                            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)}, 'your-secret')
        return jsonify({'token':token})
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