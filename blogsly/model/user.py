from sqlalchemy.ext.hybrid import hybrid_property

from blogsly.extensions import (
    db,
    bcrypt,
)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)
    articles = db.relationship('Article', back_populates='author')
    comments = db.relationship('Comment', back_populates='author')
    
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(
            self._password,
            plaintext
        )
