FROM python:3.11-alpine

COPY requirements.txt /temp/requirements.txt
COPY app /app

WORKDIR /app

RUN pip install -r /temp/requirements.txt