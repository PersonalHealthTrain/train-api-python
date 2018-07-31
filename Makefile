.PHONY: all
all:
	docker build --no-cache --rm --pull -t pht-train-api-python:latest .
	docker build --no-cache --rm --pull -t pht-train-api-python:0.1dev .

