.PHONY: all
all:
	docker build --no-cache --rm --pull -t personalhealthtrain/train-api-python:1.0rc2 .

petronetto:
	docker build --no-cache --rm --pull -t personalhealthtrain/train-api-python:1.0rc2-petronetto .

