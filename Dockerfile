FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY req.txt /code/
RUN pip install -r req.txt
COPY . /code/