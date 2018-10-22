from marshmallow import (
    Schema,
    fields,
)


class Comment(Schema):

    author = fields.Pluck(
        'User',
        'username',
        dump_only=True
    )
    article = fields.Pluck(
        'Article',
        'title',
        dump_only=True
    )
    body = fields.Str(
        required=True,
        error_messages={'required': 'Body is required.'}
    )
