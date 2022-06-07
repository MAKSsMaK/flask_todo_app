from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(100))
    todos = db.relationship('Todo', backref='user')

    def __repr__(self) -> str:
        return '<User %r>' % self.name


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'<Todo "{self.content[:20]}">'
