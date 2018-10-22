from marshmallow import (
    Schema,
    fields,
)


class User(Schema):
    
    username = fields.Str(
        required=True,
        error_messages={'required': 'Username is required.'}
    )
    password = fields.Str(
        load_only=True,
        required=True,
        error_messages={'required': 'Password is required.'}
    )
    comments = fields.Nested(
        'Comment',
        many=True,
        dump_only=True
    )
    articles = fields.Nested(
        'Article',
        many=True,
        dump_only=True
    )
