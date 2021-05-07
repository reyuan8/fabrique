# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
