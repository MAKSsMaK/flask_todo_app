import typing as t
from crypt import methods

from flask import Blueprint, redirect, render_template, request, url_for
from flask.views import MethodView
from flask_login import current_user, login_required

from . import db
from .models import Todo, User

main = Blueprint('main', __name__)


# a simple page that says hello
class ShowIndex(MethodView):
    def get(self):
        return render_template('index.html')


class ShowProfile(MethodView):
    decorators: t.List[t.Callable] = [login_required]

    def get(self):
        user_todos = current_user.todos
        print(user_todos)
        for todo in user_todos:
            print(todo.content)
        return render_template('profile.html', name=current_user.name, todos=user_todos)

    def post(self):
        user_todo = current_user.id
        content = request.form.get('content')
        new_todo = Todo(content=content, is_done=False, user_id=user_todo)
        db.session.add(new_todo)
        db.session.commit()

        return redirect(url_for('main.show_profile'))

    def delete(self):
        pass

    def put(self):
        pass


profile_view = ShowProfile.as_view('show_profile')
main.add_url_rule('/', view_func=ShowIndex.as_view('show_index'))
main.add_url_rule('/profile', view_func=profile_view)
main.add_url_rule('/profile', view_func=profile_view, methods=['POST',])
