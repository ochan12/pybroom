FROM python:3.11-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8888
CMD gunicorn -w 4 -b 0.0.0.0:8888 app:app
