# blogsly
simple blogging api with flask


## Getting Started

### Prerequisites

- `make`
- `docker`

### Deployment

```bash
make build
make run
```

## Built With
- [Flask](http://flask.pocoo.org/) - A lightweight web framework
- [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/) - For creating REST APIs
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/) - For stateless authentication via JWT
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - ORM layer
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - For object serialization/deserialization


## API

### Register User

#### url
`/auth/register`

#### method
POST

#### Data Params
example:
```json
{
  "username": "test",
  "password": "test"
}
```

#### Response
success:
```json
{
    "username": "test",
    "comments": [],
    "articles": [],
    "access_token": "MYREALLYLONGACCESSTOKEN"
}
```

### Sign in with User

#### url
`/auth/login`

#### method
POST

#### Data Params
example:
```json
{
  "username": "test",
  "password": "test"
}
```

#### Response
success:
```json
{
    "username": "test",
    "comments": [],
    "articles": [],
    "access_token": "MYREALLYLONGACCESSTOKEN"
}
```


### Create Article

#### url
`/articles`

#### method
POST

### Headers
- `Authorization`: `Bearer MYREALLYLONGACCESSTOKEN`

#### Data Params
example:
```json
{
  "title": "test",
  "body": "test"
}
```

#### Response
success:
```json
{
    "id": 1,
    "title": "test",
    "author": "test",
    "body": "test",
    "comments": []
}
```

### Create Comment

#### url
`/articles/<id:article>/comments`

#### method
POST

### Headers
- `Authorization`: `Bearer MYREALLYLONGACCESSTOKEN}`

#### Data Params
example:
```json
{
  "body": "test"
}
```

#### Response
success:
```json
{
    "author": "test",
    "body": "test",
    "article": "test"
}
```

### Read Articles

#### url
`/articles`

#### method
GET

#### Data Params
example:
```json
{
  "title": "test",
  "body": "test"
}
```

#### Response
success:
```json
[
    {
        "id": 1,
        "title": "test",
        "author": "test",
        "body": "test",
        "comments": []
    },
    {
        "id": 2,
        "title": "test2",
        "author": "test2",
        "body": "test2",
        "comments": [
            {
                "author": "test",
                "body": "test"
            }
        ]
    }
]
```

