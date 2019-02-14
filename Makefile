.PHONY: all

all: alpine pandas petronetto petronetto-deepmedic fhir

alpine:
	docker build --no-cache -f Dockerfile_alpine --rm --pull -t personalhealthtrain/train-api-python:1.0rc5-alpine .

pandas:
	docker build --no-cache -f Dockerfile_pandas --rm --pull -t personalhealthtrain/train-api-python:1.0rc5-pandas .

petronetto:
	docker build --no-cache -f Dockerfile_petronetto --rm --pull -t personalhealthtrain/train-api-python:1.0rc5-petronetto .

petronetto-deepmedic:
	docker build --no-cache -f Dockerfile_petronetto_deepmedic --rm --pull -t personalhealthtrain/train-api-python:1.0rc5-petronetto-deepmedic .

fhir:
	docker build --no-cache -f Dockerfile_fhir --rm --pull -t personalhealthtrain/train-api-python:1.0rc5-fhir .

