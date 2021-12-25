from flask import Blueprint
from controllers.user_controller import UserController

users_blueprint = Blueprint('users', __name__)

controller = UserController()


@users_blueprint.route('/users', methods=["GET"])
def listar():
    return controller.listar()

@users_blueprint.route('/users', methods=["POST"])
def criar():
    return controller.criar()
