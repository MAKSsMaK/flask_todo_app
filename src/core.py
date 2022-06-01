from flask import Blueprint
# from . import db


main = Blueprint('main', __name__)


# a simple page that says hello
@main.route('/')
def hello():
    return 'Hello, World! Page.'


@main.route('/profile')
def profile():
    return 'Profile Page'
