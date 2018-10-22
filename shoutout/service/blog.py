from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from shoutout import model
from shoutout.extensions import db
from shoutout import schema


@jwt_required
def create_article(title, body):
    identity = get_jwt_identity()
    article = model.Article(
        author=model.User.get_by_username(identity),
        title=title,
        body=body
    )
    db.session.add(article)
    db.session.commit()
    return schema.Article().dump(article)

@jwt_required
def create_comment(article_id, body):
    identity = get_jwt_identity()
    comment = model.Comment(
        author=model.User.get_by_username(identity),
        article=model.Article.query.get(article_id),
        body=body
    )
    db.session.add(comment)
    db.session.commit()
    return schema.Comment().dump(comment)

def read_articles():
    # TODO: pagination
    articles = model.Article.query.all()
    return [schema.Article().dump(article) for article in articles]
