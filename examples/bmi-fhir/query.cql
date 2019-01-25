library PhenotypeLibrary version '0.0.1'

using FHIR version '3.0.0'

codesystem "SNOMED": 'http://snomed.info/sct'
codesystem "LOINC": 'http://loinc.org'

valueset "Weight": 'vs-weight'
valueset "Height": 'vs-height'

code "Chest pain": '29857009' from "SNOMED" display 'Chest pain'
code "Weight Measured": '3141-9' from "LOINC" display 'Weight Measured'
code "Body height": '8302-2' from "LOINC" display 'Body height'

context Patient

define "In Demographic":
  InclusionCriteria

define InclusionCriteria:
  exists (
      [Condition] C
        where ToCode(C.code.coding) ~ "Chest pain"
    )
  and  ToQuantity (
    Last (
        [Observation] O
          where ToCode(O.code.coding) ~ "Weight Measured"
          sort by effective.value
      ).value as Quantity
    ).value > 50
  and  ToQuantity (
    Last (
        [Observation] O
          where ToCode(O.code.coding) ~ "Body height"
          sort by effective.value
      ).value as Quantity
    ).value > 45

define Weights:
  Last (
    [Observation: "Weight"] O
      sort by effective.value
  )

define Heights:
  Last (
    [Observation: "Height"] O
      sort by effective.value
  )

define function ToCode(coding FHIR.Coding):
  System.Code {
    code: coding.code.value,
    system: coding.system.value,
    version: coding.version.value,
    display: coding.display.value
  }

define function ToQuantity(quantity FHIR.Quantity):
  System.Quantity { value: quantity.value.value, unit: quantity.unit.value }
