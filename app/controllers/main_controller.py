from flask import Blueprint, render_template
from app.services.aluno_service import AlunoService
from app.services.professor_service import ProfessorService
from app.services.disciplina_service import DisciplinaService
from app.services.nota_service import NotaService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Página inicial / Dashboard do Sistema de Gerenciamento Acadêmico.
    Exibe estatísticas consolidadas sobre o sistema.
    """
    total_alunos = len(AlunoService.listar_todos())
    total_professores = len(ProfessorService.listar_todos())
    total_disciplinas = len(DisciplinaService.listar_todas())
    total_notas = len(NotaService.listar_todas())
    
    ultimas_notas = NotaService.listar_todas()[:5]

    return render_template(
        'index.html',
        total_alunos=total_alunos,
        total_professores=total_professores,
        total_disciplinas=total_disciplinas,
        total_notas=total_notas,
        ultimas_notas=ultimas_notas
    )
