from app.database import db
from app.models.disciplina import Disciplina

class DisciplinaService:
    """
    Camada de serviço responsável pelas regras de negócio e operações de banco de dados da entidade Disciplina.
    """

    @staticmethod
    def listar_todas():
        """Retorna todas as disciplinas ordenadas por código."""
        return Disciplina.query.order_by(Disciplina.codigo).all()

    @staticmethod
    def buscar_por_id(disciplina_id):
        """Busca uma disciplina pelo ID."""
        return db.get_or_404(Disciplina, disciplina_id)

    @staticmethod
    def criar_disciplina(nome, codigo, professor_id=None):
        """Cria uma nova disciplina."""
        if Disciplina.query.filter_by(codigo=codigo).first():
            raise ValueError("Já existe uma disciplina cadastrada com este código.")

        disciplina = Disciplina(
            nome=nome.strip(),
            codigo=codigo.strip().upper(),
            professor_id=int(professor_id) if professor_id else None
        )
        db.session.add(disciplina)
        db.session.commit()
        return disciplina

    @staticmethod
    def atualizar_disciplina(disciplina_id, nome, codigo, professor_id=None):
        """Atualiza os dados de uma disciplina existente."""
        disciplina = DisciplinaService.buscar_por_id(disciplina_id)

        disc_cod = Disciplina.query.filter_by(codigo=codigo).first()
        if disc_cod and disc_cod.id != disciplina_id:
            raise ValueError("O código informado já pertence a outra disciplina.")

        disciplina.nome = nome.strip()
        disciplina.codigo = codigo.strip().upper()
        disciplina.professor_id = int(professor_id) if professor_id else None

        db.session.commit()
        return disciplina

    @staticmethod
    def deletar_disciplina(disciplina_id):
        """Exclui uma disciplina pelo ID."""
        disciplina = DisciplinaService.buscar_por_id(disciplina_id)
        db.session.delete(disciplina)
        db.session.commit()
        return True
