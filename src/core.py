from pydoc import render_doc
from flask import Blueprint, render_template
# from . import db


main = Blueprint('main', __name__)


# a simple page that says hello
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')
