# /alunos [GET] lista os alunos
# /alunos [POST] cadastro
# /alunos/id [PUT] editar
# /alunos/id [DELETE] remover usuário
# /alunos/id [GET] lista informacões do aluno


from flask import Flask

app = Flask(__name__)


@app.route('/alunos', methods=["GET"])
def lista_alunos():
    return 'lista_alunos'


@app.route('/alunos', methods=["POST"])
def cadastro_alunos():
    return 'cadastro_alunos'


@app.route('/alunos/<int:aluno_id>', methods=["PUT"])
def editar_alunos(aluno_id):
    return 'editar'


@app.route('/alunos/<int:aluno_id>', methods=["DELETE"])
def remover_usuario(aluno_id):
    return str(aluno_id)


@app.route('/alunos/<int:aluno_id>', methods=["GET"])
def lista_informacões_do_aluno(aluno_id):
    return 'lista informacões do aluno'


if __name__ == "__main__":
    app.run(debug=True)
