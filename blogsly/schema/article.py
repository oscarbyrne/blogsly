from marshmallow import (
    Schema,
    fields,
)


class Article(Schema):

    id = fields.Integer(
        dump_only=True
    )
    author = fields.Pluck(
        'User',
        'username',
        dump_only=True
    )
    title = fields.Str(
        required=True,
        error_messages={'required': 'Title is required.'}
    )
    body = fields.Str(
        required=True,
        error_messages={'required': 'Body is required.'}
    )
    comments = fields.Nested(
        'Comment',
        only=['author', 'body'],
        many=True,
        dump_only=True
    )
