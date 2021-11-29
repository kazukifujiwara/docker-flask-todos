"""
This is a DAO module.
"""
import uuid
from schema.todo import TodoSchema
from flask import abort
from marshmallow.exceptions import ValidationError

class TodoDAO(object):
    """This is a class for DAO
    which enable users to get/create/update/delete todo objects.
    """
    def __init__(self):
        self.todos = []

    def get(self, task_id):
        for todo in self.todos:
            print(todo['task_id'])
            print(task_id)
            if todo['task_id'] == uuid.UUID(task_id):
                return todo
        abort(404, f"Todo {task_id} doesn't exist")

    def create(self, data):
        try:
            schema = TodoSchema()
            result = schema.load(data)
            result['task_id'] = uuid.uuid4()
            self.todos.append(result)
        except ValidationError as err:
            abort(400, err.messages)
        return result

    def update(self, task_id, data):
        todo = self.get(task_id)
        todo.update(data)
        return todo

    def delete(self, task_id):
        todo = self.get(task_id)
        self.todos.remove(todo)

