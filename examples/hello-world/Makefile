.PHONY: all, describe, run
all:
	docker build --rm --no-cache -t my_train:station.1 
	
describe:
	docker run --rm my_train:station.1 --station-id 1 describe

run:
	docker run --rm my_train:station.1 --station-id 1 run

