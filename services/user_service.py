from models.user import User

class UserService:

    @staticmethod
    def listar():
        usuarios = User.query.all()
        # users = [usuario.to_json() for usuario in usuarios]
        return usuarios

    @staticmethod
    def criar_usuario(nome):
        user = User(nome)

        return user.create()