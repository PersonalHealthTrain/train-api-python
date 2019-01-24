import os
import json
import csv
import string
import requests
import pandas as pd
import numpy as np
import sys
import re
from pht.internal import StationRuntimeInfo, ConjunctionBuilder
from pht.train.response import RunResponse
from pht.train import SimpleTrain
from pht.requirement import url_by_name, Require
from pht.train.response.exit_state import SUCCESS
from pht.rebase import DockerRebaseStrategy
from pht.entrypoint import cmd_for_train


model_file = '/opt/model'


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
def get_data(url, body, file_name):
    result = requests.post(url, json=body)
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
            for item in data[0]['result']:
                # print(item['valueQuantity'])
                pid = item['id']  # .strip('smart-')
                print(pid)
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



class BMITrain(SimpleTrain):
    def __init__(self):
        self.data_source = url_by_name('MY_DATA_SOURCE')

    def requirements(self) -> ConjunctionBuilder:
        return Require(self.data_source)

    def model_summary(self) -> str:
        if not os.path.exists(model_file):
            return 'No Model'
        with open(model_file, 'r') as f:
            return f.read()

    def run(self, info: StationRuntimeInfo) -> RunResponse:

        if not os.path.exists('/opt'):
            os.mkdir('/opt')
        with open(model_file, 'w') as f:
            f.write('Hello World')

        return RunResponse(
            state=SUCCESS,
            free_text_message='Hello world',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/train-api-python:1.0rc3',
                next_train_tag='station.2',
                export_files=[model_file]
            )
        )


if __name__ == '__main__':
    cmd_for_train(BMITrain())
