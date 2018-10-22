from flask_restplus import (
    Namespace,
    Resource,
)
from webargs.flaskparser import use_kwargs

from shoutout import schema
from shoutout import service


api = Namespace('auth')


@api.route('/register')
class Register(Resource):

    @use_kwargs(schema.User)
    def post(self, **kwargs):
        return service.register(**kwargs)


@api.route('/login')
class Login(Resource):

    @use_kwargs(schema.User)
    def post(self, **kwargs):
        return service.login(**kwargs)
