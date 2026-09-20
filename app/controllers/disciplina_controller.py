from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.disciplina_service import DisciplinaService
from app.services.professor_service import ProfessorService

disciplina_bp = Blueprint('disciplinas', __name__, url_prefix='/disciplinas')

@disciplina_bp.route('/')
def index():
    """Listagem de todas as disciplinas."""
    disciplinas = DisciplinaService.listar_todas()
    return render_template('disciplinas/index.html', disciplinas=disciplinas)

@disciplina_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    """Cadastro de uma nova disciplina."""
    professores = ProfessorService.listar_todos()

    if request.method == 'POST':
        nome = request.form.get('nome')
        codigo = request.form.get('codigo')
        professor_id = request.form.get('professor_id')

        try:
            DisciplinaService.criar_disciplina(nome, codigo, professor_id)
            flash('Disciplina cadastrada com sucesso!', 'success')
            return redirect(url_for('disciplinas.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('disciplinas/form.html', disciplina=None, professores=professores)

@disciplina_bp.route('/editar/<int:disciplina_id>', methods=['GET', 'POST'])
def editar(disciplina_id):
    """Edição de uma disciplina."""
    disciplina = DisciplinaService.buscar_por_id(disciplina_id)
    professores = ProfessorService.listar_todos()

    if request.method == 'POST':
        nome = request.form.get('nome')
        codigo = request.form.get('codigo')
        professor_id = request.form.get('professor_id')

        try:
            DisciplinaService.atualizar_disciplina(disciplina_id, nome, codigo, professor_id)
            flash('Disciplina atualizada com sucesso!', 'success')
            return redirect(url_for('disciplinas.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('disciplinas/form.html', disciplina=disciplina, professores=professores)

@disciplina_bp.route('/excluir/<int:disciplina_id>', methods=['POST'])
def excluir(disciplina_id):
    """Exclusão de uma disciplina."""
    try:
        DisciplinaService.deletar_disciplina(disciplina_id)
        flash('Disciplina removida com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao remover disciplina: {str(e)}', 'danger')

    return redirect(url_for('disciplinas.index'))
