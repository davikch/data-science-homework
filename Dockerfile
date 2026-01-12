# https://hub.docker.com/_/python/#how-to-use-this-image

FROM python:3

WORKDIR ./app

COPY generator/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY generator .
COPY .env .

CMD [ "python", "-u", "database_operations.py", "20", "5"]
