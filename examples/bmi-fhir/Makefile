.PHONY: all, describe, run
all:
	docker build --rm --no-cache -t bmi-fhir:station.1 .
	
describe:
	docker run --rm bmi-fhir:station.1 --station-id 1 describe

run:
	docker run -e TERMINOLOGY='http://menzel.informatik.rwth-aachen.de:8080/baseDstu3' -e CQL='http://menzel.informatik.rwth-aachen.de:8082/cql/evaluate' -e DATA='http://menzel.informatik.rwth-aachen.de:8080/baseDstu3/'  bmi-fhir:station.1 --station-id 1 run

