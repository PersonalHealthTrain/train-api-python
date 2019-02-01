from SPARQLWrapper import SPARQLWrapper, JSON


def run_cohort_counter(endpoint_url):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery("""
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix ncit: <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#>
        prefix roo: <http://www.cancerdata.org/roo/>
        prefix icd: <http://purl.bioontology.org/ontology/ICD10/>

        select ?patient ?ageDiagnosis
        where {
            ?patient rdf:type ncit:C16960.
            ?patient roo:100008 ?disease.
            ?disease rdf:type icd:C20.
            
            ?patient roo:100016 ?ageDiagnosisRes.
            ?ageDiagnosisRes roo:100042 ?ageDiagnosis.
        }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    sum_age = sum(int(result["ageDiagnosis"]["value"]) for result in results["results"]["bindings"])

    # divide sumAge by all patients
    cohort_size = len(results["results"]["bindings"])
    mean_age = sum_age / cohort_size

    # write output to file
    return {
        'cohortCount': cohort_size,
        'meanAge': mean_age
    }
