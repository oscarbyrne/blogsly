from flask_restplus import (
    Namespace,
    Resource,
)
from webargs.flaskparser import use_kwargs

from shoutout import schema
from shoutout import service


api = Namespace('articles')


@api.route('')
class Articles(Resource):

    @use_kwargs(schema.Article)
    def post(self, **kwargs):
        return service.create_article(**kwargs)

    def get(self):
        return service.read_articles()


@api.route('/<int:article_id>/comments')
class Comments(Resource):

    @use_kwargs(schema.Comment)
    def post(self, article_id, **kwargs):
        return service.create_comment(article_id, **kwargs)
