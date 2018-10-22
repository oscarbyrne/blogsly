from os import environ


class Config():
    SECRET_KEY = environ['BLOGSLY_SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False # To suppress flask warning for new default
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DEBUG = False

class Production(Config):
    ENV = 'production'

class Development(Config):
    ENV = 'development'
    DEBUG = True
