import os
from flask import Flask
from app.database import db
from app.controllers import main_bp, aluno_bp, professor_bp, disciplina_bp, nota_bp

def create_app(config=None):
    """
    Application Factory para o projeto Flask.
    Configura a instância do Flask, banco de dados SQLAlchemy e registra os Blueprints.
    """
    app = Flask(__name__)

    # Configurações padrão
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave-secreta-desenvolvimento-kodland')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///academico.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config:
        app.config.update(config)

    # Inicializar o banco de dados
    db.init_app(app)

    # Registrar os Blueprints de cada funcionalidade
    app.register_blueprint(main_bp)
    app.register_blueprint(aluno_bp)
    app.register_blueprint(professor_bp)
    app.register_blueprint(disciplina_bp)
    app.register_blueprint(nota_bp)

    # Criar as tabelas no banco SQLite se não existirem
    with app.app_context():
        db.create_all()

    return app
