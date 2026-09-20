from app.database import db
from datetime import datetime, timezone

class Nota(db.Model):
    """
    Modelo de dados para representar a Nota lançada para um Aluno em uma Disciplina.
    Princípio SRP: Armazenamento da associação entre Aluno, Disciplina e a pontuação obtida.
    """
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    data_lancamento = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)

    def __repr__(self):
        return f'<Nota {self.valor} - Aluno ID: {self.aluno_id} - Disciplina ID: {self.disciplina_id}>'
