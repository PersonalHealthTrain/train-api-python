define docker_build
    docker build --no-cache --rm --pull -t personalhealthtrain/train-api-python:1.0rc10-$(1) -f dockerfiles/Dockerfile_$(1) .
endef

.PHONY: all alpine pandas petronetto petronetto-deepmedic fhir

all: alpine pandas petronetto petronetto-deepmedic fhir

alpine:
	$(call docker_build,alpine)

pandas:
	$(call docker_build,pandas)

petronetto:
	$(call docker_build,petronetto)

petronetto-deepmedic:
	$(call docker_build,petronetto-deepmedic)

fhir:
	$(call docker_build,fhir)
