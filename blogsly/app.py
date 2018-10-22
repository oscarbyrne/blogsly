from os import environ

from flask import Flask

from blogsly.extensions import *

from blogsly import api


def create_app():
    app = Flask(__name__)
    load_config(app)
    init_extensions(app)
    setup_hooks(app)
    api.init_app(app)
    return app


def load_config(app):
    ENV = environ.get(
        'FLASK_ENV',
        'production'
    )
    app.config.from_object(
        f'blogsly.config.{ENV.title()}'
    )

def init_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

def setup_hooks(app):
    @app.before_first_request
    def create_tables():
        db.create_all()
