FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /api
COPY requirements.txt /api
RUN pip install -r requirements.txt --no-cache-dir
COPY . /api
