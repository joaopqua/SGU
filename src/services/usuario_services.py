from src import db
from ..models import usuario_model
from ..schemas import usuario_eschema


def cadastrar_usuario(usuario):
    usuario_db = usuario_model.Usuario(nome = usuario.nome, email = usuario.email, telefone= usuario.telefone)
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

def listar_usuario():
    usuarios = usuario_model.Usuario.query.all()
    schema = usuario_eschema.UsuarioSchema()
    return usuarios

def listar_usuario_id():
    ...

def excluir_usuario():
    ...

def editar_usuario():
    ...

def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email = email).first()