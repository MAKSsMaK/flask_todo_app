import typing as t

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.views import MethodView
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import User

auth = Blueprint('auth', __name__)


class ShowLogin(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login data you entered and try again.')
            return redirect(url_for('auth.show_login'))

        login_user(user, remember=remember)
        return redirect(url_for('main.show_profile'))


class ShowRegistration(MethodView):
    def get(self):
        return render_template('register.html')

    def post(self):
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.show_register'))

        new_user = User(name=name, age=age, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth_login'))


class Logout(MethodView):
    decorators: t.List[t.Callable] = [login_required]

    def get(self):
        logout_user()
        return redirect(url_for('main.show_index'))


login_view = ShowLogin.as_view('show_login')
register_view = ShowRegistration.as_view('show_register')
logout_view = Logout.as_view('logout')

auth.add_url_rule('/login', view_func=login_view)
auth.add_url_rule('/login', view_func=login_view, methods=['POST',])

auth.add_url_rule('/register', view_func=register_view)
auth.add_url_rule('/register', view_func=register_view, methods=['POST',])

auth.add_url_rule('/logout', view_func=logout_view)
