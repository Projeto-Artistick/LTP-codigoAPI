from flask import Flask
from routes.atividade_routes import atividade_bp
from routes.usuario_routes import usuario_bp
from routes.historico_routes import historico_bp
from utils.error_handlers import register_error_handlers

app = Flask(__name__)

# Registrando os blueprints
app.register_blueprint(atividade_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(historico_bp)

# Registrando handlers de erro personalizados
register_error_handlers(app)

if __name__ == '__main__':
    app.run(debug=True)