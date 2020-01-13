FROM python:3.7.5-buster

WORKDIR /

COPY . /

RUN pip install -r requirements.txt

EXPOSE ${APP_PORT}

CMD ["python", "./src/server.py"]