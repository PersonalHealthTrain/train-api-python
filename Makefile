.PHONY: all

all: alpine petronetto petronetto-deepmedic

alpine:
	docker build --no-cache -f Dockerfile --rm --pull -t personalhealthtrain/train-api-python:1.0rc3 .

petronetto:
	docker build --no-cache -f Dockerfile_petronetto --rm --pull -t personalhealthtrain/train-api-python:1.0rc3-petronetto .

petronetto-deepmedic:
	docker build --no-cache -f Dockerfile_petronetto_deepmedic --rm --pull -t personalhealthtrain/train-api-python:1.0rc3-petronetto-deepmedic .

