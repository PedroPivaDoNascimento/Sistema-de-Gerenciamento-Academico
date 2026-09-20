# Sistema de Gerenciamento Acadêmico

Este é um projeto completo de **Sistema de Gerenciamento Acadêmico** construído utilizando o framework **Flask** em Python.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Framework Web:** Flask 3.1.3
- **ORM / Banco de Dados:** Flask-SQLAlchemy 3.1.1 (SQLite)
- **Frontend / Interface:** HTML5, Jinja2, Bootstrap 5 e Font Awesome 6
---



## 📚 Módulos e Funcionalidades

### 1. 🎓 Módulo de Alunos
- **Cadastro:** Inclusão de alunos com validação de matrícula e e-mail únicos.
- **Listagem:** Tabela com todos os alunos cadastrados.
- **Edição:** Atualização de dados pessoais.
- **Exclusão:** Remoção do aluno e remoção em cascata de suas notas associadas.

### 2. 👨‍🏫 Módulo de Professores
- **Cadastro:** Cadastro de corpo docente com nome, e-mail e departamento.
- **Listagem:** Visualização dos professores cadastrados.
- **Edição:** Atualização dos dados do professor.
- **Exclusão:** Remoção do professor desvinculando-o das disciplinas atribuídas.

### 3. 📖 Módulo de Disciplinas
- **Cadastro:** Cadastro de disciplinas com código único (ex: `MAT101`) e associação opcional a um professor responsável.
- **Listagem:** Exibição das disciplinas e seus respetivos professores.
- **Edição:** Atualização de dados e alteração de professor responsável.
- **Exclusão:** Exclusão da disciplina e de suas avaliações/notas associadas.

### 4. 📝 Módulo de Notas
- **Lançamento:** Atribuição de notas (de `0.0` a `10.0`) associando um **Aluno** a uma **Disciplina**.
- **Listagem & Consulta:** Filtro de notas por aluno específico ou visualização geral.
- **Edição:** Ajuste de pontuações de notas já lançadas.
- **Exclusão:** Remoção do registro de nota.

---

## 🛠️ Passo a Passo de Instalação e Execução

### 1. Clonar ou Acessar o Diretório do Projeto
```bash
cd "(path do diretório)"
```

### 2. Criar e Ativar um Ambiente Virtual (Venv)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Inicialização do Banco de Dados e Servidor
O banco de dados SQLite (`academico.db` dentro de `instance/`) é automaticamente criado e inicializado na primeira execução através da Application Factory (`db.create_all()`).

Para rodar a aplicação localmente:
```bash
python main.py
```
Acesse no navegador: **`http://localhost:5000`** ou **`http://127.0.0.1:5000`**

---

## 📐 Padrões Arquiteturais Aplicados

- **MVC (Model-View-Controller):**
  - **Model:** Definição dos esquemas das tabelas (`app/models`).
  - **View:** Páginas web renderizadas em Jinja2 com Bootstrap (`app/templates`).
  - **Controller:** Blueprints do Flask manipulando as requisições HTTP (`app/controllers`).
- **Camada de Serviço (Service Pattern - SRP):**
  - Cada entidade possui um serviço dedicado (`app/services`) que isola toda a regra de negócio e chamadas de banco de dados, mantendo os Controllers enxutos e focados no fluxo HTTP.
