FROM python:3.6

LABEL maintainer="Cassi <cassipanda@gmail.com>"

# Create Directory
RUN mkdir -p /usr/src/scrabble
WORKDIR /usr/src/scrabble
RUN ls -a


COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt


COPY . /usr/src/scrabble
COPY wait-for-it.sh /wait-for-it.sh
COPY /startup/run.sh /run.sh
RUN chmod +x /wait-for-it.sh
RUN chmod +x /run.sh

EXPOSE 80
