from blogsly.extensions import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.Integer, db.ForeignKey('users.username'))
    author = db.relationship('User', back_populates='comments')
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    article = db.relationship('Article', back_populates='comments')
