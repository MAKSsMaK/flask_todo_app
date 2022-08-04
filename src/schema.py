from . import marsh
from .models import Todo, User


class TodoSchema(marsh.SQLAlchemySchema):
    class Meta:
        model = Todo

    content = marsh.auto_field()
    user_id = marsh.auto_field()
    is_done = marsh.auto_field()
    

class UserSchema(marsh.SQLAlchemySchema):
    class Meta:
        model = User

    name = marsh.auto_field()
    todos = marsh.Nested(TodoSchema, many=True)
