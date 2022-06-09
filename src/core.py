import typing as t

from flask import Blueprint, redirect, render_template, request, url_for, flash
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
    methods: t.Optional[t.List[str]] = ['GET', 'POST']

    def get(self, **kwargs):
        user_todos = current_user.todos
        return render_template('profile.html', name=current_user.name, todos=user_todos)

    def post(self):
        user_todo = current_user.id
        content = request.form.get('content')
        if not content:
            flash('You can not create empty task!')
            return redirect(url_for('main.show_profile'))
        new_todo = Todo(content=content, is_done=False, user_id=user_todo)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('main.show_profile'))


class UpdateProfileTodo(MethodView):
    decorators: t.List[t.Callable] = [login_required]
    methods: t.Optional[t.List[str]] = ['POST']

    def post(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.is_done = not todo.is_done
        db.session.commit()
        return redirect(url_for('main.show_profile'))


class DeleteProfileTodo(MethodView):
    decorators: t.List[t.Callable] = [login_required]
    methods: t.Optional[t.List[str]] = ['GET']

    def get(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('main.show_profile'))


profile_view = ShowProfile.as_view('show_profile')
profile_update = UpdateProfileTodo.as_view('update_profile')
profile_delete = DeleteProfileTodo.as_view('delete_profile')

main.add_url_rule('/', view_func=ShowIndex.as_view('show_index'))
main.add_url_rule('/profile', view_func=profile_view)
main.add_url_rule('/profile', view_func=profile_view)
main.add_url_rule('/profile/update/<int:todo_id>', view_func=profile_update)
main.add_url_rule('/profile/delete/<int:todo_id>', view_func=profile_delete)
