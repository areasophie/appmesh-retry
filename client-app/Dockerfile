FROM python:3.8.5-buster

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./ /app

EXPOSE 5000

CMD gunicorn app:app -c gunicorn_settings.py

