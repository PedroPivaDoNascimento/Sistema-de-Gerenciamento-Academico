from app.database import db

class Aluno(db.Model):
    """
    Modelo de dados para representar um Aluno no sistema acadêmico.
    Princípio SRP: Representa exclusivamente o esquema de dados do Aluno no banco.
    """
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relacionamento de 1 para N com Nota (se o aluno for excluído, as notas relacionadas são removidas)
    notas = db.relationship('Nota', backref='aluno', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Aluno {self.nome} - Matrícula: {self.matricula}>'
