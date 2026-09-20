from app.database import db
from app.models.professor import Professor

class ProfessorService:
    """
    Camada de serviço responsável pelas regras de negócio e persistência da entidade Professor.
    """

    @staticmethod
    def listar_todos():
        """Retorna todos os professores ordenados por nome."""
        return Professor.query.order_by(Professor.nome).all()

    @staticmethod
    def buscar_por_id(professor_id):
        """Busca um professor pelo ID."""
        return db.get_or_404(Professor, professor_id)

    @staticmethod
    def criar_professor(nome, email, departamento):
        """Cria um novo professor no sistema."""
        if Professor.query.filter_by(email=email).first():
            raise ValueError("Já existe um professor cadastrado com este e-mail.")

        professor = Professor(
            nome=nome.strip(),
            email=email.strip().lower(),
            departamento=departamento.strip()
        )
        db.session.add(professor)
        db.session.commit()
        return professor

    @staticmethod
    def atualizar_professor(professor_id, nome, email, departamento):
        """Atualiza os dados de um professor existente."""
        professor = ProfessorService.buscar_por_id(professor_id)

        prof_email = Professor.query.filter_by(email=email).first()
        if prof_email and prof_email.id != professor_id:
            raise ValueError("O e-mail informado já está em uso por outro professor.")

        professor.nome = nome.strip()
        professor.email = email.strip().lower()
        professor.departamento = departamento.strip()

        db.session.commit()
        return professor

    @staticmethod
    def deletar_professor(professor_id):
        """Exclui um professor pelo ID (desvincula de disciplinas se houver)."""
        professor = ProfessorService.buscar_por_id(professor_id)
        for disciplina in professor.disciplinas:
            disciplina.professor_id = None
        db.session.delete(professor)
        db.session.commit()
        return True
