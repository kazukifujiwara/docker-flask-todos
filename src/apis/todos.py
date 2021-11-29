"""
This is an api module.
"""
import csv

from utils.format import TimeFormat
from flask_restx import Namespace, Resource, fields
from dao.todo import TodoDAO

api = Namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'task_id': fields.String(readonly=True,
                        description='The task unique identifier',
                        example='fdc02467-67df-4577-9ceb-d9a18acc0587'),
    'task': fields.String(required=True,
                         description='The task name',
                         example='Build an API'),
    'status': fields.String(required=True,
                         description='The task status (new/pending/done)',
                         example='new'),
    'created_at': TimeFormat(readonly=True,
                            description='The task created',
                            example='2021-08-09 18:19:23'),
    'detail': fields.String(required=False,
                         description='The task detail',
                         example='This is sample task\'s detail')
})

DAO = TodoDAO()

# Load test data
with open('test/sample_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        DAO.create(r)

@api.route('/')
class TodoList(Resource):
    @api.expect(todo)
    @api.marshal_with(todo, code=201)
    def post(self):
        return DAO.create(api.payload), 201

    @api.doc('clist_todos')
    @api.marshal_list_with(todo)
    def get(self):
        return DAO.todos

@api.route('/<string:task_id>')
@api.response(404, 'Todo not found')
@api.param('task_id', 'The task identifier')
class Todo(Resource):
    """This is Todo class
    """
    @api.doc('get_todo')
    @api.marshal_with(todo)
    def get(self, task_id):
        return DAO.get(task_id)

    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, task_id):
        DAO.delete(task_id)
        return '', 204

    @api.expect(todo)
    @api.marshal_with(todo)
    def put(self, task_id):
        return DAO.update(task_id, api.payload)
