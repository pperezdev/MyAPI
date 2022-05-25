FROM python:3.8

WORKDIR /tmp

COPY . /tmp

ARG env_flask_variable_web=main.py 

ENV FLASK_MY_API=$env_flask_variable_web 

RUN pip install -r requirements.txt