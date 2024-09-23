from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta

# Base de dados fictícia com senhas armazenadas em hash
fake_users_db = {
    "user": {
        "username": "user",
        "role": "user",
        "password_hash": generate_password_hash("L0XuwPOdS5U")
    },
    "admin": {
        "username": "admin",
        "role": "admin",
        "password_hash": generate_password_hash("JKSipm0YH")
    },
}

# Função para autenticar o usuário
def authenticate_user():
    try:
        # Extraindo credenciais do corpo da requisição
        auth = request.get_json()
        if not auth or not auth.get("username") or not auth.get("password"):
            return None, {"msg": "Both username and password are required"}, 400
        
        username = auth.get("username")
        password = auth.get("password")

        # Buscando usuário no banco de dados fictício
        user = fake_users_db.get(username)
        if not user:
            return None, {"msg": "User not found"}, 404
        
        # Verificando a senha (hash)
        if not check_password_hash(user['password_hash'], password):
            return None, {"msg": "Incorrect password"}, 401

        # Retornar o usuário se a autenticação for bem-sucedida
        return username, user, 200

    except Exception as e:
        return None, {"msg": f"An error occurred during authentication: {str(e)}"}, 500
