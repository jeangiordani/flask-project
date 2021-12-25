from flask import Flask

import mysql.connector

from database.db import db


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:9177@localhost/flask"
db.init_app(app)


from routes.user_routes import users_blueprint


app.register_blueprint(users_blueprint)


if __name__ == '__main__':
    app.run(debug=True)

