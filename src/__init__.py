from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
marsh = Marshmallow()

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:1111@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'palyanyza'

db.init_app(app)
migrate.init_app(app, db)

marsh.init_app(app)

login_manager.login_view = 'auth.login'
login_manager.init_app(app)


from .models import User


# get user by primary-key
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# auth blueprint
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# core blueprint
from .core import main as main_blueprint
app.register_blueprint(main_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
