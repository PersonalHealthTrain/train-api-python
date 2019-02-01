import json
import fhir
import sparql
import os

# The PHT API dependencies
from pht.train import SimpleTrain
from pht.internal import StationRuntimeInfo, ConjunctionBuilder
from pht.train.response import RunResponse
from pht.requirement.env import enum_by_name, token_by_name, url_by_name
from pht.requirement import Require
from pht.train.response.exit_state import SUCCESS
from pht.rebase import DockerRebaseStrategy
from pht.entrypoint import cmd_for_train

_FHIR = 'FHIR'
_SPARQL = 'SPARQL'


class Train(SimpleTrain):
    def __init__(self):

        # Declare all the properties that the Train cares about
        self.endpoint_type = enum_by_name('ENDPOINT_TYPE', choices=[_FHIR, _SPARQL])
        self.endpoint_url = url_by_name('ENDPOINT_URL')
        self.endpoint_token = token_by_name('ENDPOINT_TOKEN')
        self.output_file = '/opt/train/output.txt'

    def requirements(self) -> ConjunctionBuilder:
        # Declare the requirements of this train. The station needs to provide:
        #   * The endpoint type (either 'FHIR' or 'SPARQL'
        #   * The endpoint url
        #   * The endpoint token
        return Require(self.endpoint_type) & Require(self.endpoint_url) & Require(self.endpoint_token)

    def model_summary(self) -> str:
        if os.path.exists(self.output_file):
            with open(self.output_file, 'r') as f:
                return '\n'.join(f.readlines())
        return 'Currently no model available'

    def run(self, info: StationRuntimeInfo) -> RunResponse:

        # get the values provided by the station platform
        endpoint_type = self.endpoint_type.get_value()
        endpoint_url = self.endpoint_url.get_value()
        endpoint_token = self.endpoint_token.get_value()

        # Run the cohort counter
        output_json = {}
        if endpoint_type == _FHIR:
            output_json = fhir.runCohortCounter(endpoint_url, endpoint_token)
        elif endpoint_type == _SPARQL:
            output_json = sparql.runCohortCounter(endpoint_url)

        # Write output to file
        with open(self.output_file, 'w') as f:
            f.write(json.dumps(output_json))

        return RunResponse(
            state=SUCCESS,
            free_text_message='Algorithm has been executed successfully',
            rebase=DockerRebaseStrategy(
                frm='TODO correct train',
                next_train_tags=['train-tag'],
                export_files=[self.output_file]))


if __name__ == '__main__':
    cmd_for_train(Train())
