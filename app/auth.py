from functools import wraps
from flask import request, jsonify
from firebase_admin import auth


def check_firebase_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        id_token = request.headers.get('Authorization')
        if not id_token:
            return jsonify({'error': 'Authorization token is missing'}), 401
        try:
            decoded_token = auth.verify_id_token(id_token)
            request.user = decoded_token
        except Exception as e:
            return jsonify({'error': str(e)}), 403
        return f(*args, **kwargs)
    return wrapper
