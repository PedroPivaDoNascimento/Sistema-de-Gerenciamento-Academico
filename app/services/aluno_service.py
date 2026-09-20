from app.database import db
from app.models.aluno import Aluno

class AlunoService:
    """
    Camada de serviço responsável pelas regras de negócio e operações de banco de dados da entidade Aluno.
    Garante o desacoplamento entre os Controllers e os Models (SOLID/SRP).
    """

    @staticmethod
    def listar_todos():
        """Retorna a lista de todos os alunos ordenados por nome."""
        return Aluno.query.order_by(Aluno.nome).all()

    @staticmethod
    def buscar_por_id(aluno_id):
        """Busca um aluno pelo ID."""
        return db.get_or_404(Aluno, aluno_id)

    @staticmethod
    def criar_aluno(nome, matricula, email):
        """Cria um novo aluno no sistema com validação simples de duplicidade."""
        if Aluno.query.filter_by(matricula=matricula).first():
            raise ValueError("Já existe um aluno cadastrado com esta matrícula.")
        if Aluno.query.filter_by(email=email).first():
            raise ValueError("Já existe um aluno cadastrado com este e-mail.")

        aluno = Aluno(nome=nome.strip(), matricula=matricula.strip(), email=email.strip().lower())
        db.session.add(aluno)
        db.session.commit()
        return aluno

    @staticmethod
    def atualizar_aluno(aluno_id, nome, matricula, email):
        """Atualiza os dados de um aluno existente."""
        aluno = AlunoService.buscar_por_id(aluno_id)

        # Verificar se a matrícula ou email pertencem a outro aluno
        aluno_mat = Aluno.query.filter_by(matricula=matricula).first()
        if aluno_mat and aluno_mat.id != aluno_id:
            raise ValueError("A matrícula informada já está em uso por outro aluno.")

        aluno_email = Aluno.query.filter_by(email=email).first()
        if aluno_email and aluno_email.id != aluno_id:
            raise ValueError("O e-mail informado já está em uso por outro aluno.")

        aluno.nome = nome.strip()
        aluno.matricula = matricula.strip()
        aluno.email = email.strip().lower()

        db.session.commit()
        return aluno

    @staticmethod
    def deletar_aluno(aluno_id):
        """Exclui um aluno pelo ID."""
        aluno = AlunoService.buscar_por_id(aluno_id)
        db.session.delete(aluno)
        db.session.commit()
        return True
