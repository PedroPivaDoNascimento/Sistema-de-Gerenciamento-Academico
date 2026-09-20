from app.database import db

class Professor(db.Model):
    """
    Modelo de dados para representar um Professor no sistema acadêmico.
    Princípio SRP: Representa exclusivamente a estrutura de dados do Professor.
    """
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    departamento = db.Column(db.String(100), nullable=False)

    # Relacionamento de 1 para N com Disciplina
    disciplinas = db.relationship('Disciplina', backref='professor', lazy=True)

    def __repr__(self):
        return f'<Professor {self.nome} - {self.departamento}>'
