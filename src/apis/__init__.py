from flask_restx import Api
from .todos import api as todos

api = Api(
    version='1.0',
    title='Sample API',
    description='A sample API',
    doc="/doc/"
)

api.add_namespace(todos, path='/api/todos')