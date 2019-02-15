.PHONY: all, describe, run
all:
	docker build --rm --no-cache -t hello-world:station.1 .
	
describe:
	docker run --rm hello-world:station.1 --station-id 1 describe

run:
	docker run hello-world:station.1 --station-id 1 run
