FROM python:3.7.2-alpine3.8
LABEL maintainer="luk.zim91@gmail.com"

COPY . /tmp/pht
WORKDIR /tmp/pht
RUN python setup.py install && cd / && && rm -rf /tmp/* /var/tmp/*
