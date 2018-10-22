from flask import jsonify

from flask_restplus import Api
import flask_jwt_extended.exceptions as jwt_extended_exception
import jwt.exceptions as jwt_exception

from shoutout import controller


api = Api(
    title='shoutout',
    version='1.0',
)

api.add_namespace(controller.ns_auth)
api.add_namespace(controller.ns_blog)


# patch jwt exception handlers (see: https://github.com/vimalloc/flask-jwt-extended/issues/86)
@api.errorhandler(jwt_extended_exception.NoAuthorizationError)
def handle_auth_error(e):
    return {'message': str(e)}, 401

@api.errorhandler(jwt_extended_exception.CSRFError)
def handle_auth_error(e):
    return {'message': str(e)}, 401

@api.errorhandler(jwt_exception.ExpiredSignatureError)
def handle_expired_error(e):
    return {'message': 'Token has expired'}, 401

@api.errorhandler(jwt_extended_exception.InvalidHeaderError)
def handle_invalid_header_error(e):
    return {'message': str(e)}, 422

@api.errorhandler(jwt_exception.InvalidTokenError)
def handle_invalid_token_error(e):
    return {'message': str(e)}, 422

@api.errorhandler(jwt_extended_exception.JWTDecodeError)
def handle_jwt_decode_error(e):
    return {'message': str(e)}, 422

@api.errorhandler(jwt_extended_exception.WrongTokenError)
def handle_wrong_token_error(e):
    return {'message': str(e)}, 422

@api.errorhandler(jwt_extended_exception.RevokedTokenError)
def handle_revoked_token_error(e):
    return {'message': 'Token has been revoked'}, 401

@api.errorhandler(jwt_extended_exception.FreshTokenRequired)
def handle_fresh_token_required(e):
    return {'message': 'Fresh token required'}, 401

@api.errorhandler(jwt_extended_exception.UserLoadError)
def handler_user_load_error(e):
    # The identity is already saved before this exception was raised,
    # otherwise a different exception would be raised, which is why we
    # can safely call get_jwt_identity() here
    identity = get_jwt_identity()
    return {'message': "Error loading the user {}".format(identity)}, 401

@api.errorhandler(jwt_extended_exception.UserClaimsVerificationError)
def handle_failed_user_claims_verification(e):
    return {'message': 'User claims verification failed'}, 400


def init_app(app):
    api.init_app(app)
    
    # patch webargs exception handler (see: https://github.com/sloria/webargs/issues/255)
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

