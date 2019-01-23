.PHONY: all

all: alpine petronetto

alpine:
	docker build --no-cache --rm --pull -t personalhealthtrain/train-api-python:1.0rc3 .

petronetto:
	docker build --no-cache --rm --pull -t personalhealthtrain/train-api-python:1.0rc3-petronetto .

