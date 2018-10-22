# API

## Register User

### Url
`/auth/register`

### Method
POST

### Data Params
example:
```json
{
  "username": "test",
  "password": "test"
}
```

### Response
success:
```json
{
    "username": "test",
    "comments": [],
    "articles": [],
    "access_token": "MYREALLYLONGACCESSTOKEN"
}
```

## Sign in with User

### Url
`/auth/login`

### Method
POST

### Data Params
example:
```json
{
  "username": "test",
  "password": "test"
}
```

### Response
success:
```json
{
    "username": "test",
    "comments": [],
    "articles": [],
    "access_token": "MYREALLYLONGACCESSTOKEN"
}
```


## Create Article

### Url
`/articles`

### Method
POST

### Headers
- `Authorization`: `Bearer MYREALLYLONGACCESSTOKEN`

### Data Params
example:
```json
{
  "title": "test",
  "body": "test"
}
```

### Response
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

## Create Comment

### Url
`/articles/<id:article>/comments`

### Method
POST

### Headers
- `Authorization`: `Bearer MYREALLYLONGACCESSTOKEN}`

### Data Params
example:
```json
{
  "body": "test"
}
```

### Response
success:
```json
{
    "author": "test",
    "body": "test",
    "article": "test"
}
```

## Read Articles

### Url
`/articles`

### Method
GET

### Data Params
example:
```json
{
  "title": "test",
  "body": "test"
}
```

### Response
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
