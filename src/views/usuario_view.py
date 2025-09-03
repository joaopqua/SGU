from flask_restful import Resource
from marshmallow import ValidationError
from ..schemas import usuario_eschema
from flask import request, jsonify, make_response
from ..services import usuario_services
from src import api
from ..models.usuario_model import Usuario


# POST-GET-PUT-DELETE
# lidar com todos os usuarios
class UsuarioList(Resource):
    def get(self):
        usuarios = usuario_services.listar_usuario()

        if not usuarios:
            return make_response(jsonify({f'message':'não existe usuários!'}))
        
        schema = usuario_eschema.UsuarioSchema(many = True)

        return make_response(jsonify(schema.dump(usuarios)),200)

    def post(self):
        schema = usuario_eschema.UsuarioSchema()

        try:
            dados = schema.load(request.json)

        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        if usuario_services.listar_usuario_email(dados['email']):
            return make_response(jsonify({'message':'Email já cadastrado!'}), 400)
        
        try:
            #criação do novo usuário no baco
            novo_usuario = Usuario(
                nome = dados['nome'],
                email = dados['email'],
                telefone = dados['telefone'],
                senha = dados['senha']
            )

            resultado = usuario_services.cadastrar_usuario(novo_usuario)
            return make_response(jsonify(schema.dump(resultado)), 201)
        
        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(UsuarioList, '/usuario')
