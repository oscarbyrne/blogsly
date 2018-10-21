from flask import jsonify

from flask_restplus import Api

from shoutout.controller.auth import api as ns_auth


api = Api(
    title='shoutout',
    version='1.0',
)

api.add_namespace(ns_auth)


def init_app(app):
    api.init_app(app)

    # from: https://github.com/sloria/webargs/issues/255
    # fixes returning webargs messages as json for 422 errors
    @app.errorhandler(422)
    def handle_unprocessable_entity(err):
        # webargs attaches additional metadata to the `data` attribute
        exc = getattr(err, "exc")
        if exc:
            # Get validations from the ValidationError object
            messages = exc.messages
        else:
            messages = ["Invalid request"]
        return jsonify({"messages": messages}), 422
