from blogsly.extensions import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.Integer, db.ForeignKey('users.username'))
    author = db.relationship('User', back_populates='articles')
    comments = db.relationship('Comment', back_populates='article')
