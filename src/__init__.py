from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:1111@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# auth blueprint
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# core blueprint
from .core import main as main_blueprint
app.register_blueprint(main_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
