from shoutout.model.user import User
from shoutout.extensions import db
from shoutout.schema.auth import UserAuth


def register(username, password):
    user = User(
        username=username,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return login(username, password)

def login(username, password):
    user = User.get_by_username(username)
    if user.check_password(password):
        return UserAuth().dump(user)
    else:
        raise NotImplementedError() # TODO
