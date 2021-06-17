FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY . .

