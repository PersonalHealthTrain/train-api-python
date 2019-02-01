.PHONY: all, describe, run
all:
	docker build --rm --no-cache -t train_pht_on_fhir:station.1 .
	
describe:
	docker run --rm train_pht_on_fhir:station.1 --station-id 1 describe

run:
	docker run -e ENDPOINT_TYPE=FHIR -e ENDPOINT_URL=http://hapi.fhir.org/baseDstu3 -e ENDPOINT_TOKEN=my_web_app  train_pht_on_fhir:station.1 --station-id 1 run

