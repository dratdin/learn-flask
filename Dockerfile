FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 5000
EXPOSE 27017

CMD ["flask", "run", "--host=0.0.0.0"]
