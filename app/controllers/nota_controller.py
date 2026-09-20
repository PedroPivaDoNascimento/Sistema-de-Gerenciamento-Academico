from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.nota_service import NotaService
from app.services.aluno_service import AlunoService
from app.services.disciplina_service import DisciplinaService

nota_bp = Blueprint('notas', __name__, url_prefix='/notas')

@nota_bp.route('/')
def index():
    """Listagem e consulta de notas lançadas."""
    aluno_id = request.args.get('aluno_id', type=int)
    alunos = AlunoService.listar_todos()

    if aluno_id:
        notas = NotaService.buscar_por_aluno(aluno_id)
        aluno_selecionado = AlunoService.buscar_por_id(aluno_id)
    else:
        notas = NotaService.listar_todas()
        aluno_selecionado = None

    return render_template(
        'notas/index.html',
        notas=notas,
        alunos=alunos,
        aluno_selecionado=aluno_selecionado
    )

@nota_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    """Lançamento de uma nova nota associando aluno e disciplina."""
    alunos = AlunoService.listar_todos()
    disciplinas = DisciplinaService.listar_todas()

    if request.method == 'POST':
        aluno_id = request.form.get('aluno_id', type=int)
        disciplina_id = request.form.get('disciplina_id', type=int)
        valor = request.form.get('valor')

        try:
            NotaService.lançar_nota(aluno_id, disciplina_id, valor)
            flash('Nota lançada com sucesso!', 'success')
            return redirect(url_for('notas.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template(
        'notas/form.html',
        nota=None,
        alunos=alunos,
        disciplinas=disciplinas
    )

@nota_bp.route('/editar/<int:nota_id>', methods=['GET', 'POST'])
def editar(nota_id):
    """Edição do valor de uma nota."""
    nota = NotaService.buscar_por_id(nota_id)

    if request.method == 'POST':
        valor = request.form.get('valor')

        try:
            NotaService.atualizar_nota(nota_id, valor)
            flash('Nota atualizada com sucesso!', 'success')
            return redirect(url_for('notas.index'))
        except ValueError as e:
            flash(str(e), 'danger')

    return render_template('notas/form.html', nota=nota, alunos=[], disciplinas=[])

@nota_bp.route('/excluir/<int:nota_id>', methods=['POST'])
def excluir(nota_id):
    """Exclusão de uma nota lançada."""
    try:
        NotaService.deletar_nota(nota_id)
        flash('Nota removida com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao remover nota: {str(e)}', 'danger')

    return redirect(url_for('notas.index'))
