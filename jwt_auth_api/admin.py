from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from fake_services import get_admin_data

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/admin", methods=["GET"])
@jwt_required()
def admin():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"msg": "Permission denied"}), 403
    admin_data = get_admin_data()
    return jsonify(admin_data), 200
