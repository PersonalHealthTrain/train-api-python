FROM python:3.6.6-alpine3.8

COPY . /opt/pht
WORKDIR /opt/pht
RUN python setup.py install && rm -rf /opt

