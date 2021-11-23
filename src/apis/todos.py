from utils.format import TimeFormat
from flask_restx import Namespace, Resource, fields
from dao.todo import TodoDAO

api = Namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.String(readonly=True,
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
DAO.create({'status': 'done', 'task': 'ADD function', 'detail': 'implement task-add function.'})
DAO.create({'status': 'done', 'task': 'UPDATE function', 'detail': 'implement task-update function.'})
DAO.create({'status': 'done', 'task': 'DELETE function', 'detail': 'implement task-delete function.'})
DAO.create({'status': 'done', 'task': 'change task\'s status (to done)', 'detail': 'implement status-change function.\n(new)->(done)'})
DAO.create({'status': 'done', 'task': 'change task\'s status (to new)', 'detail': 'implement status-change function.\n(done)->(new)'})
DAO.create({'status': 'pending', 'task': 'Implement Login Function', 'detail': 'implement Login function'})
DAO.create({'status': 'new', 'task': 'Support for Multiple TODO List', 'detail': 'switching to multiple todo lists.'})

DAO.create({'status': 'new', 'task': 'Task01' , 'detail': 'Task01'})
DAO.create({'status': 'new', 'task': 'Task02' , 'detail': 'Task02'})
DAO.create({'status': 'new', 'task': 'Task03' , 'detail': 'Task03'})
DAO.create({'status': 'new', 'task': 'Task04' , 'detail': 'Task04'})
DAO.create({'status': 'pending', 'task': 'Task05' , 'detail': 'Task05'})
DAO.create({'status': 'pending', 'task': 'Task06' , 'detail': 'Task06'})
DAO.create({'status': 'pending', 'task': 'Task07' , 'detail': 'Task07'})
DAO.create({'status': 'pending', 'task': 'Task08' , 'detail': 'Task08'})
DAO.create({'status': 'done', 'task': 'Task09' , 'detail': 'Task09'})
DAO.create({'status': 'done', 'task': 'Task10' , 'detail': 'Task10'})
DAO.create({'status': 'done', 'task': 'Task11' , 'detail': 'Task11'})
DAO.create({'status': 'done', 'task': 'Task12' , 'detail': 'Task12'})

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
