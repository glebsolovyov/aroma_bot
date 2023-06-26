FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV YTHONUNBUFFERED 1

COPY requirements.txt temp/requirements.txt
COPY bot /bot

WORKDIR bot

RUN pip install -r /temp/requirements.txt