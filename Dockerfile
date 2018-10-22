FROM python:3.7-alpine

COPY requirements.txt requirements.txt

RUN apk update && \
    apk add --virtual .build-deps gcc musl-dev libffi-dev && \
    pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY blogsly blogsly
COPY .flaskenv .env ./

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
