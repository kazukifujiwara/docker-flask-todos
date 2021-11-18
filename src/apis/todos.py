from utils.format import TimeFormat
from flask_restx import Namespace, Resource, fields
from dao.todo import TodoDAO

api = Namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.String(readonly=True,
                        description='The task unique identifier',
                        example='fdc02467-67df-4577-9ceb-d9a18acc0587'),
    'task': fields.String(required=True,
                         description='The task details',
                         example='Build an API'),
    'created_at': TimeFormat(readonly=True,
                            description='The task created',
                            example='2021-08-09 18:19:23')
})

DAO = TodoDAO()
DAO.create({'task': 'Task01'})
DAO.create({'task': 'Task02'})
DAO.create({'task': 'Task03'})

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

@api.route('/<string:id>')
@api.response(404, 'Todo not found')
@api.param('id', 'The task identifier')
class Todo(Resource):
    @api.doc('get_todo')
    @api.marshal_with(todo)
    def get(self, id):
        return DAO.get(id)

    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, id):
        DAO.delete(id)
        return '', 204

    @api.expect(todo)
    @api.marshal_with(todo)
    def put(self, id):
        return DAO.update(id, api.payload)