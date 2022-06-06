import typing as t

from flask import Blueprint, render_template
from flask.views import MethodView
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


# a simple page that says hello
class ShowIndex(MethodView):
    def get(self):
        return render_template('index.html')


class ShowProfile(MethodView):
    decorators: t.List[t.Callable] = [login_required]

    def get(self):
        return render_template('profile.html', name=current_user.name)


main.add_url_rule('/', view_func=ShowIndex.as_view('show_index'))
main.add_url_rule('/profile', view_func=ShowProfile.as_view('show_profile'))
