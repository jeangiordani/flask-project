from flask import request, jsonify
from services.user_service import UserService
from schemas.user_schema import user_schema, users_schema


class UserController:
    service = None

    def __init__(self):
        self.service = UserService()

    def listar(self):
        # service = UserService()
        users = self.service.listar()
        users = users_schema.dump(users)
        # print()
        return jsonify(status="OK", usuarios = users), 200

    def criar(self):
        body = request.get_json()
        nome = body.get('name', None)

        if len(nome) < 5:
            return jsonify(status="Failed", message= "O tamanho do nome deve ser maior que 5"), 422

        usuario = self.service.criar_usuario(nome)
        user = user_schema.dump(usuario)

        return jsonify(status="Created", usuario=user), 201
