import datetime as dt
from marshmallow import Schema, fields

class TodoSchema(Schema):
    task = fields.Str(
        required=True,
        error_messages={'required': {'message': '[task] is required.'}}
    )
    created_at = fields.DateTime(missing=dt.datetime.now)
