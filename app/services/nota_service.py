from app.database import db
from app.models.nota import Nota
from app.models.aluno import Aluno
from app.models.disciplina import Disciplina

class NotaService:
    """
    Camada de serviço responsável pelas regras de negócio e operações de banco de dados da entidade Nota.
    Garante o lançamento, associação e consulta das notas de forma desacoplada.
    """

    @staticmethod
    def listar_todas():
        """Retorna todas as notas lançadas com a associação de Alunos e Disciplinas."""
        return Nota.query.order_by(Nota.data_lancamento.desc()).all()

    @staticmethod
    def buscar_por_id(nota_id):
        """Busca uma nota pelo ID."""
        return db.get_or_404(Nota, nota_id)

    @staticmethod
    def lançar_nota(aluno_id, disciplina_id, valor):
        """Lança uma nova nota associando Aluno e Disciplina."""
        try:
            valor_float = float(valor)
        except ValueError:
            raise ValueError("O valor da nota deve ser um número válido.")

        if valor_float < 0.0 or valor_float > 10.0:
            raise ValueError("O valor da nota deve estar entre 0.0 e 10.0.")

        aluno = db.session.get(Aluno, aluno_id)
        if not aluno:
            raise ValueError("Aluno não encontrado.")

        disciplina = db.session.get(Disciplina, disciplina_id)
        if not disciplina:
            raise ValueError("Disciplina não encontrada.")

        nota = Nota(
            aluno_id=aluno_id,
            disciplina_id=disciplina_id,
            valor=valor_float
        )
        db.session.add(nota)
        db.session.commit()
        return nota

    @staticmethod
    def atualizar_nota(nota_id, valor):
        """Atualiza o valor de uma nota existente."""
        nota = NotaService.buscar_por_id(nota_id)

        try:
            valor_float = float(valor)
        except ValueError:
            raise ValueError("O valor da nota deve ser um número válido.")

        if valor_float < 0.0 or valor_float > 10.0:
            raise ValueError("O valor da nota deve estar entre 0.0 e 10.0.")

        nota.valor = valor_float
        db.session.commit()
        return nota

    @staticmethod
    def deletar_nota(nota_id):
        """Exclui uma nota pelo ID."""
        nota = NotaService.buscar_por_id(nota_id)
        db.session.delete(nota)
        db.session.commit()
        return True

    @staticmethod
    def buscar_por_aluno(aluno_id):
        """Retorna todas as notas de um aluno específico."""
        return Nota.query.filter_by(aluno_id=aluno_id).order_by(Nota.data_lancamento.desc()).all()
