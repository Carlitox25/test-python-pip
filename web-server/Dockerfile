FROM python:3.10

WORKDIR /web
COPY requirements.txt /web/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web/requirements.txt

COPY . /web

CMD {"uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80"}d