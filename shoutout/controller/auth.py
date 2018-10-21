from flask_restplus import (
    Namespace,
    Resource,
)
from webargs.flaskparser import use_kwargs

import shoutout.schema.auth as schema
import shoutout.service.auth as service


api = Namespace('auth')


@api.route('/register')
class Register(Resource):

    @use_kwargs(schema.UserAuth)
    def post(self, **kwargs):
        return service.register(**kwargs)


@api.route('/login')
class Login(Resource):

    @use_kwargs(schema.UserAuth)
    def post(self, **kwargs):
        return service.login(**kwargs)
