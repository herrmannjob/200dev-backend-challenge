from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from fake_services import check_health
from auth import authenticate_user
from users import user_bp
from admin import admin_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# Rotas de saúde
@app.route("/health", methods=["GET"])
def health():
    health_status = check_health()
    return jsonify(health_status), 200

# Rota para geração de token JWT
@app.route("/token", methods=["POST"])
def login():
    result = authenticate_user()
    
    # Se autenticação foi bem-sucedida
    if result[0]:
        username, user, status_code = result
        access_token = create_access_token(
            identity={"username": username, "role": user["role"]}, 
            expires_delta=timedelta(hours=1)
        )
        return jsonify(access_token=access_token), status_code
    
    # Caso contrário, retorne a mensagem de erro e o status
    return jsonify(result[1]), result[2]

# Rotas protegidas
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
