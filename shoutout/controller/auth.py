from flask_restplus import (
    Namespace,
    Resource,
)

api = Namespace('auth')


@api.route('/login')
class Login(Resource):

    def post(self):
        return 'hello'
