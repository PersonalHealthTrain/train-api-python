# We use V1 RC4 for implementing the train.
# Also, we use the -fhir image such that the fhirclient and SPAQRLWrapper modules are available
FROM personalhealthtrain/train-api-python:1.0rc5-fhir
LABEL maintainer="luk.zim91@gmail.com"

# Copy all required source code files for the train inside the image
COPY entrypoint.py /opt/entrypoint.py
COPY sparql.py /opt/sparql.py
COPY fhir.py /opt/fhir.py

ENTRYPOINT ["python", "/opt/entrypoint.py"]
