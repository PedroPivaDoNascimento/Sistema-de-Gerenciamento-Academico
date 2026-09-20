from flask_sqlalchemy import SQLAlchemy

# Instância do SQLAlchemy compartilhada na aplicação (Padrão Singleton/Extension)
db = SQLAlchemy()
