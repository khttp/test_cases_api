import jwt 
from functools import wraps
from flask import request, jsonify
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        print(auth)
        if auth is None:
           return jsonify({'message':'Token is missing'}),401
        try:
            data=jwt.decode(auth.split(' ')[1],'your-secret',algorithms=['HS256'])
            print(data)
        except Exception as e:
            return jsonify({'Error':f'Error {e}'}),401
        return f(*args, **kwargs)
    return decorated
