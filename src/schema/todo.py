"""
This is a schema module.
"""
import datetime as dt
from marshmallow import Schema, fields

class TodoSchema(Schema):
    """This is TodoSchema class
    which defines fields' type, required flag and error messages.
    """
    task = fields.Str(
        required=True,
        error_messages={'required': {'message': '[task] is required.'}}
    )
    status = fields.Str(
        required=True,
        error_messages={'required': {'message': '[status] is required.'}}
    )
    detail = fields.Str(
        required=False,
        error_messages={'required': {'message': 'Some error occurred with tasks\' [detail].'}}
    )
    created_at = fields.DateTime(missing=dt.datetime.now)
