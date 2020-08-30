FROM python:3-alpine

WORKDIR /app
COPY . /app
RUN pip3 install -r requirement.txt

CMD [ "python3", "-u", "server.py" ]