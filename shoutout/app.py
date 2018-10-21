from os import environ

from flask import Flask

from shoutout.extensions import *

from shoutout import api


def create_app():
    app = Flask(__name__)
    set_config(app)
    init_extensions(app)
    setup_hooks(app)
    api.init_app(app)
    return app


def set_config(app):
    # TODO: set config from file (support different environments)
    app.config['SECRET_KEY'] = environ.get('SHOUTOUT_SECRET_KEY', '')

def init_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

def setup_hooks(app):
    @app.before_first_request
    def create_tables():
        db.create_all()
