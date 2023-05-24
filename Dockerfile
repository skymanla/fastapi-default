# image name fastapi-default
# docker build -t fastapi-default:latest .
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./log.ini /code/log.ini

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt