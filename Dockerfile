FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt
COPY . /code/