from app.database import db

class Disciplina(db.Model):
    """
    Modelo de dados para representar uma Disciplina.
    Princípio SRP: Estruturação dos dados pertinentes à disciplina acadêmica.
    """
    __tablename__ = 'disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=True)

    # Relacionamento de 1 para N com Nota
    notas = db.relationship('Nota', backref='disciplina', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Disciplina {self.codigo} - {self.nome}>'
