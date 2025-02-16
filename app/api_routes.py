from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models import User
from datetime import timedelta

api = Blueprint('api', __name__)

@api.route('/api/login', methods=['POST'])
def api_login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()

    if user and user.verify_password(password):
        access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(hours=24))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Login failed. Check your email and password."}), 401

@api.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if user:
        return jsonify({"msg": f"This is a protected route. User ID: {current_user_id}, User Name: {user.nome}"}), 200
    else:
        return jsonify({"msg": "User not found"}), 404