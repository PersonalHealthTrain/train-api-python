FROM python:3.6.6-alpine3.8
LABEL maintainer="luk.zim91@gmail.com"

COPY . /opt/pht
WORKDIR /opt/pht
RUN python setup.py install && rm -rf /opt /tmp/* /var/tmp/*
WORKDIR /
