# blogsly
simple blogging api with flask


## Getting Started

### Prerequisites

- `make`
- `docker`

### Deployment

```bash
echo BLOGSLY_SECRET_KEY=$YOURSECRETPHRASE > .env
make build
make run
```
The API will now be running in a docker container serving on port 5000

## Built With
- [Flask](http://flask.pocoo.org/) - A lightweight web framework
- [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/) - For creating REST APIs
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/) - For stateless authentication via JWT
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - ORM layer
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - For object serialization/deserialization
- [Generic Docker Makefile](https://github.com/ekalinin/github-markdown-toc) - For docker image management

## Documentation

The API endpoints are documented [here.](API.md)
