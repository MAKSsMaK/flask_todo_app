from enum import unique
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self) -> str:
        return '<User %r>' % self.name
