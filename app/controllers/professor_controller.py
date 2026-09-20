from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.professor_service import ProfessorService

professor_bp = Blueprint('professores', __name__, url_prefix='/professores')

@professor_bp.route('/')
def index():
    """Listagem de todos os professores."""
    professores = ProfessorService.listar_todos()
    return render_template('professores/index.html', professores=professores)

@professor_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    """Cadastro de um novo professor."""
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        departamento = request.form.get('departamento')

        try:
            ProfessorService.criar_professor(nome, email, departamento)
            flash('Professor cadastrado com sucesso!', 'success')
            return redirect(url_for('professores.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('professores/form.html', professor=None)

@professor_bp.route('/editar/<int:professor_id>', methods=['GET', 'POST'])
def editar(professor_id):
    """Edição de um professor."""
    professor = ProfessorService.buscar_por_id(professor_id)

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        departamento = request.form.get('departamento')

        try:
            ProfessorService.atualizar_professor(professor_id, nome, email, departamento)
            flash('Dados do professor atualizados com sucesso!', 'success')
            return redirect(url_for('professores.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('professores/form.html', professor=professor)

@professor_bp.route('/excluir/<int:professor_id>', methods=['POST'])
def excluir(professor_id):
    """Exclusão de um professor."""
    try:
        ProfessorService.deletar_professor(professor_id)
        flash('Professor removido com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao remover professor: {str(e)}', 'danger')

    return redirect(url_for('professores.index'))
