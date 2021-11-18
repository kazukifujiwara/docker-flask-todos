import uuid
from schema.todo import TodoSchema
from flask import abort
from marshmallow.exceptions import ValidationError

class TodoDAO(object):
    def __init__(self):
        # self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            print(todo['id'])
            print(id)
            if todo['id'] == uuid.UUID(id):
                return todo
        abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        try:
            schema = TodoSchema()
            result = schema.load(data)
            result['id'] = uuid.uuid4()
            self.todos.append(result)
        except ValidationError as err:
            abort(400, err.messages)
        return result

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)