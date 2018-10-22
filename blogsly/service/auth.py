from flask_jwt_extended import create_access_token

from blogsly import model
from blogsly.extensions import db
from blogsly import schema


def register(username, password):
    user = model.User(
        username=username,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return login(username, password)

def login(username, password):
    user = model.User.get_by_username(username)
    if user.check_password(password):
        dump = schema.User().dump(user)
        dump['access_token'] = create_access_token(identity=username)
        return dump
    else:
        raise NotImplementedError() # TODO
