.PHONY: all
all:
	docker build --no-cache --rm --pull -t personalhealthtrain/train-api-python:0.2 .
	docker tag personalhealthtrain/train-api-python:0.2 personalhealthtrain/train-api-python:latest

