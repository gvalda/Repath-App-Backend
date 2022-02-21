FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE true
ENV PYTHONUNBUFFERED true

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .