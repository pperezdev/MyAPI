FROM python:3.8

WORKDIR /tmp

COPY . /tmp

ARG env_flask_variable_web=main.py 

ENV FLASK_APP=$env_flask_variable_web 

RUN pip install -r requirements.txt

EXPOSE 7825

CMD ["flask", "run", "--host=0.0.0.0", "-p 5000"]