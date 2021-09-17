FROM python:latest

COPY . /app/

RUN useradd -m 10000
USER 10000
