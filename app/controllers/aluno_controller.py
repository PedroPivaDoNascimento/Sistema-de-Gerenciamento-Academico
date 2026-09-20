from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.aluno_service import AlunoService

aluno_bp = Blueprint('alunos', __name__, url_prefix='/alunos')

@aluno_bp.route('/')
def index():
    """Listagem de todos os alunos."""
    alunos = AlunoService.listar_todos()
    return render_template('alunos/index.html', alunos=alunos)

@aluno_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    """Cadastro de um novo aluno."""
    if request.method == 'POST':
        nome = request.form.get('nome')
        matricula = request.form.get('matricula')
        email = request.form.get('email')

        try:
            AlunoService.criar_aluno(nome, matricula, email)
            flash('Aluno cadastrado com sucesso!', 'success')
            return redirect(url_for('alunos.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('alunos/form.html', aluno=None)

@aluno_bp.route('/editar/<int:aluno_id>', methods=['GET', 'POST'])
def editar(aluno_id):
    """Edição dos dados de um aluno."""
    aluno = AlunoService.buscar_por_id(aluno_id)

    if request.method == 'POST':
        nome = request.form.get('nome')
        matricula = request.form.get('matricula')
        email = request.form.get('email')

        try:
            AlunoService.atualizar_aluno(aluno_id, nome, matricula, email)
            flash('Dados do aluno atualizados com sucesso!', 'success')
            return redirect(url_for('alunos.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('alunos/form.html', aluno=aluno)

@aluno_bp.route('/excluir/<int:aluno_id>', methods=['POST'])
def excluir(aluno_id):
    """Exclusão de um aluno."""
    try:
        AlunoService.deletar_aluno(aluno_id)
        flash('Aluno removido com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao remover aluno: {str(e)}', 'danger')

    return redirect(url_for('alunos.index'))
