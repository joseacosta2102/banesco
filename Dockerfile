FROM python:3.11.2-buster

ENV DEBIAN_FRONTEND='noninteractive'

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 14000