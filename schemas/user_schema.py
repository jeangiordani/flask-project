from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome")

user_schema = UserSchema()
users_schema = UserSchema(many= True)