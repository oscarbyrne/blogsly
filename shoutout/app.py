from flask import Flask

from shoutout.extensions import *

from shoutout.api import api


def create_app():
    app = Flask(__name__)
    init_extensions(app)
    setup_hooks(app)
    api.init_app(app)
    return app


def init_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)

def setup_hooks(app):
    @app.before_first_request
    def create_tables():
        db.create_all()
