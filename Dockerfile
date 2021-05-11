FROM python:3.9.2-buster

RUN mkdir /flaskapp

WORKDIR /flaskapp

ADD ./flask-example .

RUN python -m pip install --upgrade pip && \
	pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
