import os
import json
import csv
import requests
import pandas as pd
import numpy as np
import re
from pht.internal import StationRuntimeInfo
from pht.train.response import RunResponse
from pht.train import SimpleTrain
from pht.train.response.exit_state import SUCCESS
from pht.rebase import DockerRebaseStrategy
from pht.entrypoint import cmd_for_train


def _path(filename: str):
    # For now, store everything in /opt
    return os.path.join('/opt', filename)


# Parse CQL expression so that CQL evaluation engine can resolve them
with open('/opt/query.cql', "r+") as f:
    CQL = f.read()
    CQL = CQL.replace('\\"', '"')
    CQL = CQL.replace('\\\\/', '/')
    CQL = CQL.replace('\\\\"', "'")
    CQL = CQL[0:len(CQL) - 1]


# External webservices
# CQL evaluation engine
cqlEngineURL = "http://menzel.informatik.rwth-aachen.de:8082/cql/evaluate"

# URL to FHIR server
dataServiceUri = "http://menzel.informatik.rwth-aachen.de:8080/baseDstu3/"

# Terminology Server
terminologyServiceUri = "http://menzel.informatik.rwth-aachen.de:8080/baseDstu3/"


# Send HTTP POST request to FHIR server and get FHIR resource bundle in JSON format
def get_data(body, file_name):
    result = requests.post(cqlEngineURL, json=body)
    with open(file_name, 'w') as outfile:
        json.dump(result.text, outfile, ensure_ascii=False)
    print('A JSON file has been retrieved and saved!')


# Preprocessed unstructured JSON data
def preprocess_data(json_file_name, preprocess_json_file_name, temp_csv_file_name):
    with open(json_file_name, "r+") as f:
        old = f.read()
        old = old.replace('\\"', '"')
        old = old.replace('\\\\/', '/')
        old = old.replace('\\\\"', "'")
        old = old[1:len(old) - 1]

    with open(preprocess_json_file_name, "w") as f:
        f.write(old)

    with open(preprocess_json_file_name) as f:
        data = json.load(f)

    with open(temp_csv_file_name, 'w', newline='') as csvfile:
        fieldnames = ['Patient id', 'Weight', 'Height', 'Name', 'DOB', 'Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data[0]['result']:
            pid = item['id']
            print(pid)
            try:
                name = item['name'][0]['given'][0] + " " + item['name'][0]['given'][1] + " " + item['name'][0]['family']
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


# Use the preprocessed data to compute something. It shows BMI calculation
def compute_bmi(temp_csv_file, bmi_file):
    pid = []
    weight = []
    height = []

    with open(temp_csv_file) as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        next(csv_reader)

        for row in csv_reader:
            pid.append(row[0])
            height.append(float(row[2]) / 100)
            weight.append(float(row[1]))

        pid_arr = np.asarray(pid)
        weight_arr = np.asarray(weight)
        height_arr = np.asarray(height)

        bmi = []
        for i in range(0, len(height_arr)):
            if 0 < weight_arr[i] and 0 < height_arr[i] < 2.72:
                bmi_calc = round(weight_arr[i] / (height_arr[i] ** 2), 1)
                bmi.append(bmi_calc)
            else:
                raise ValueError('Invalid height or weight')

        body_mass_index = bmi
        bmi_arr = np.asarray(body_mass_index)

        bmi_df = pd.DataFrame({'BMI': bmi_arr})
        pid_df = pd.DataFrame({'PID': pid_arr})

        pid_df.reset_index(drop=True, inplace=True)
        bmi_df.reset_index(drop=True, inplace=True)

        final_df = pd.concat([pid_df, bmi_df], axis=1)

        # print(finalDF)
        final_df.to_csv(bmi_file, sep=',', encoding='utf-8', index=False)
        print('BMI file has been generated!')


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

        json_file = '/opt/data.json'
        # Send HTTP Post request to the FHIR Server
        get_data({
            "code": CQL,
            "terminologyServiceUri": terminologyServiceUri,
            "dataServiceUri": dataServiceUri,
            'Content-Type': 'application/json'
        }, json_file)

        preprocess_json_file = _path('temp.json')
        temp_csv_file = _path('test.csv')
        preprocess_data(json_file, preprocess_json_file, temp_csv_file)

        input_phenotype = temp_csv_file
        compute_bmi(temp_csv_file=input_phenotype, bmi_file=self.bmi_file)

        return RunResponse(
            state=SUCCESS,
            free_text_message='BMI values have been computed successfully',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/train-api-python:1.0rc3-pandas',
                next_train_tag='station.2',
                export_files=[self.bmi_file]
            )
        )


if __name__ == '__main__':
    cmd_for_train(BMITrain())
