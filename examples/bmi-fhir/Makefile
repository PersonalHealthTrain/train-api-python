.PHONY: all, describe, run
all:
	docker build --rm --no-cache -t bmi-fhir:station.1 .
	
describe:
	docker run --rm bmi-fhir:station.1 --station-id 1 describe

run:
	docker run  bmi-fhir:station.1 --station-id 1 run

