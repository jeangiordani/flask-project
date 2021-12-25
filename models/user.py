from database.db import db

class User(db.Model):

    def __init__(self,nome: str):
        self.nome = nome

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }

    def __repr__(self):
        return '<User %r>' % self.nome

    def create(self):
        db.session.add(self)
        db.session.commit()

        return self