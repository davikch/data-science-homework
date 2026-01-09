# https://hub.docker.com/_/python/#how-to-use-this-image

FROM python:3

WORKDIR .

COPY src/requirements.txt ./
RUN pip install -r requirements.txt

COPY src .

CMD [ "python", "-u", "database_operations.py"]
