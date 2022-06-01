from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer)

    def __repr__(self) -> str:
        return '<User %r>' % self.name
