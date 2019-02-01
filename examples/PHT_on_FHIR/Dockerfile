FROM personalhealthtrain/train-api-python:1.0rc4-fhir
LABEL maintainer="luk.zim91@gmail.com"

COPY entrypoint.py /opt/entrypoint.py
COPY sparql.py /opt/sparql.py
COPY fhir.py /opt/fhir.py

ENTRYPOINT ["python", "/opt/entrypoint.py"]

