from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from fake_services import get_user_data

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/user", methods=["GET"])
@jwt_required()
def user():
    identity = get_jwt_identity()
    if identity["role"] != "user":
        return jsonify({"msg": "Permission denied"}), 403
    user_data = get_user_data()
    return jsonify(user_data), 200
