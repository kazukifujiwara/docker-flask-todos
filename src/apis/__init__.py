from flask_restx import Api
from .todos import api as todos

api = Api(
    version='1.0',
    title='Sample TODO API',
    description='Sample TODO API',
    doc="/doc/"
)

api.add_namespace(todos, path='/api/todos')