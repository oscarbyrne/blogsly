from marshmallow import (
    Schema,
    fields,
)
from flask_jwt_extended import create_access_token


class UserAuth(Schema):

    username = fields.Str(
        required=True,
        error_messages={'required': 'Username is required.'}
    )
    password = fields.Str(
        load_only=True,
        required=True,
        error_messages={'required': 'Password is required.'}
    )
    token = fields.Function(
        dumps_only=True,
        serialize=lambda user: create_access_token(identity=user.username)
    )
