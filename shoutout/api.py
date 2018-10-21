from flask_restplus import Api

from shoutout.controller.auth import api as ns_auth


api = Api(
    title='shoutout',
    version='1.0',
)

api.add_namespace(ns_auth)
