#!/usr/bin/env python
# coding: utf-8
import json
import csv
import requests
import pandas as pd
import numpy as np
import re
import os

from pht.train import SimpleTrain
from pht.internal import StationRuntimeInfo
from pht.train.response import RunResponse
from pht.train.response.RunExit import SUCCESS
from pht.rebase import DockerRebaseStrategy
from pht.entrypoint import cli_for_train


# Parse CQL expression so that CQL evaluation engine can resolve them
def parse_cql():
    with open('/opt/query.cql', "r+") as f:
        old = f.read()
        old = old.replace('\\"', '"')
        old = old.replace('\\\\/', '/')
        old = old.replace('\\\\"', "'")
        old = old[0:len(old) - 1]
    return old


# Send HTTP POST request to FHIR server and get FHIR resource bundle in JSON format
def getData(URL, body, file_name):
    result = requests.post(URL, data=json.dumps(body))

    with open(file_name, 'w') as outfile:
        json.dump(result.text, outfile, ensure_ascii=False)

    print('A JSON file has been retreived and saved!')


# Preprocessed unstructured JSON data
def preprocessData(json_file_name, preprocess_json_file_name, temp_csv_file_name):
    with open(json_file_name, "r+") as f:
        old = f.read()
        old = old.replace('\\"', '"')
        old = old.replace('\\\\/', '/')
        old = old.replace('\\\\"', "'")
        old = old[1:len(old) - 1]

        f.close()

        with open(preprocess_json_file_name, "w") as f:
            f.write(old)
            f.close()
        f = open(preprocess_json_file_name)
        data = json.load(f)

        f.close()
        with open(temp_csv_file_name, 'w', newline='') as csvfile:
            fieldnames = ['Patient id', 'Weight', 'Height', 'Name', 'DOB', 'Gender']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            print(data)
            for item in data[0]['result']:
                # print(item['valueQuantity'])
                pid = item['id']  # .strip('smart-')
                try:
                    name = item['name'][0]['given'][0] + " " + item['name'][0]['given'][1] + " " + item['name'][0][
                        'family']
                except:
                    name = 'null'

                if re.search('\d+-\d\d-\d+', item['birthDate']):
                    birthDate = item['birthDate']
                else:
                    birthDate = '0-0-0'

                if (re.search('(female|male)', item['gender'])):
                    gender = item['gender']
                else:
                    gender = 'null'

                if re.search("\d+.\d+ kg", str(data[5]['result'])):
                    weight = 0
                    for witem in data[5]['result']:

                        if witem['subject']['reference'] != ("Patient/" + pid):
                            weight = 'null'
                        else:
                            weight = witem['valueQuantity']['value']
                            break
                else:
                    weight = 'null'

                if re.search("\d+.\d+ cm", str(data[6]['result'])):

                    height = 0
                    for hitem in data[6]['result']:
                        if hitem['subject']['reference'] != ("Patient/" + pid):
                            height = 'null'
                        else:
                            height = hitem['valueQuantity']['value']
                            break
                else:
                    height = 'null'

                writer.writerow({'Patient id': pid, 'Weight': weight, 'Height': height, 'Name': name, 'DOB': birthDate,
                                 'Gender': gender})


# In[5]:


# Use the preprocessed data to compute something. It shows BMI calculation
def computeBMI(temp_csv_file, BMI_file):
    PID = []
    weight = []
    height = []

    with open(temp_csv_file) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        next(csvReader)

        for row in csvReader:
            PID.append(row[0])
            height.append(float(row[2]) / 100)
            weight.append(float(row[1]))

        PID_arr = np.asarray(PID)
        weight_arr = np.asarray(weight)
        height_arr = np.asarray(height)

        BMI = []
        for i in range(0, len(height_arr)):
            if 0 < weight_arr[i] and 0 < height_arr[i] < 2.72:
                BMI_calc = round(weight_arr[i] / height_arr[i] ** 2, 1)
                BMI.append(BMI_calc)
            else:
                raise ValueError('Invalid height or weight')

        body_mass_index = BMI
        BMI_arr = np.asarray(body_mass_index)

        bmiDF = pd.DataFrame({'BMI': BMI_arr})
        pidDF = pd.DataFrame({'PID': PID_arr})

        pidDF.reset_index(drop=True, inplace=True)
        bmiDF.reset_index(drop=True, inplace=True)

        finalDF = pd.concat([pidDF, bmiDF], axis=1)

        # print(finalDF)
        finalDF.to_csv(BMI_file, sep=',', encoding='utf-8', index=False)
        print('BMI file has been generated!')


# In[6]:

# Provide the URL to CQL evaluation engine
cqlEngineURL = "http://menzel.informatik.rwth-aachen.de:8082/cql/evaluate"

# Provide the URL to FHIR server
dataServiceUri = "http://menzel.informatik.rwth-aachen.de:8080/baseDstu3/"


# A FHIR terminology service is simply a set of functions built on the definitions provided by a collection of CodeSystem,
# ValueSet and ConceptMap resources, with additional inherently known terminologies providing support.
# The terminology service builds on the basic principles for using terminologies in FHIR,
# which comes with the support of Terminology Service Capability Statement Implementers should be familiar with:
# -- Using codes in FHIR
# -- The CodeSystem resource
# -- The ValueSet resource
# -- The ConceptMap resource
# It's mostly a RESTful Terminology Server
terminologyServiceUri = "http://menzel.informatik.rwth-aachen.de:8080/baseDstu3/"  # Holds our CodeSystem/ValueSet/ConceptMap resources


CQL = parse_cql()


def _path(filename: str):
    return os.path.join('/opt/train', filename)


class BMITrain(SimpleTrain):
    def __init__(self):
        self.bmi_file = _path('BMI1.csv')

    # Currently, this train does not declare any requirements
    def requirements(self):
        pass

    def model_summary(self) -> str:
        if os.path.exists(self.bmi_file):
            with open(self.bmi_file, 'r') as bmi_file_handle:
                return '\n'.join(bmi_file_handle.readlines())
        return 'No BMIs available in this train!'

    def run(self, info: StationRuntimeInfo) -> RunResponse:

        cqlCode = parse_cql()
        # Generating JSON body for HTTP POST request to FHIR server
        queryBody = {
            "code": cqlCode,
            "terminologyServiceUri": terminologyServiceUri,
            "dataServiceUri": dataServiceUri,
            'Content-Type': 'application/json'
        }

        # print(queryBody)
        # Not the model, save to /tmp
        json_to_save = '/tmp/data.json'
        # print(str(queryBody))

        getData(cqlEngineURL, queryBody, json_to_save)

        input_json_file_name = json_to_save
        # Not the model, save to /tmp
        preprocess_json_file = '/tmp/temp.json'
        temp_csv_file = '/tmp/test.csv'

        preprocessData(input_json_file_name, preprocess_json_file, temp_csv_file)

        input_phenotype = temp_csv_file
        computeBMI(temp_csv_file=input_phenotype, BMI_file=self.bmi_file)

        return RunResponse(
                run_exit=SUCCESS,
                free_text_message='BMI values have been computed successfully',
                rebase=DockerRebaseStrategy(
                    frm='personalhealthtrain/train-api-python:1.0rc3-pandas',
                    next_train_tags='station.2',
                    export_files=[self.bmi_file]
                )
            )


if __name__ == '__main__':
    cli_for_train(BMITrain())
