# We use the -fhir image such that the fhirclient and SPAQRLWrapper modules are available
FROM personalhealthtrain/train-api-python:1.0rc8-fhir
LABEL maintainer="luk.zim91@gmail.com"

# Copy all required source code files for the train inside the image
COPY entrypoint.py /opt/pht_train/algorithm/entrypoint.py
COPY sparql.py /opt/pht_train/algorithm/sparql.py
COPY fhir.py /opt/pht_train/algorithm/fhir.py

ENTRYPOINT ["python", "/opt/pht_train/algorithm/entrypoint.py"]
