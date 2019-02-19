import fhir
import sparql

# The PHT API dependencies
from pht.train import SimpleDockerTrain
from pht.train.component import ConjunctionBuilder, StationRuntimeInfo
from pht.requirement import Require
from pht.requirement.environment_variable import enum_by_name, url_by_name, token_by_name
from pht.entrypoint import cli_for_train

_FHIR = 'FHIR'
_SPARQL = 'SPARQL'


class Train(SimpleDockerTrain):
    def __init__(self):
        super().__init__('PHT on FHIR', '1.0', 'TODO correct train', ['train-tag'])
        # Declare all the properties that the Train cares about
        self.endpoint_type = enum_by_name('ENDPOINT_TYPE', choices=[_FHIR, _SPARQL])
        self.endpoint_url = url_by_name('ENDPOINT_URL')
        self.endpoint_token = token_by_name('ENDPOINT_TOKEN')

        # The output of the train as trainfile
        self.output = self.model_file('output')

    def run_algorithm(self, info: StationRuntimeInfo, log):

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

        self.output.write_as_json(output_json)
        log.set_free_text_message('Algorithm has been executed successfully')

    def requirements(self) -> ConjunctionBuilder:
        # Declare the requirements of this train. The station needs to provide:
        #   * The endpoint type (either 'FHIR' or 'SPARQL'
        #   * The endpoint url
        #   * The endpoint token
        return Require(self.endpoint_type) & Require(self.endpoint_url) & Require(self.endpoint_token)

    def model_summary(self) -> str:
        return self.output.read_or_default('No result file in this version')


if __name__ == '__main__':
    cli_for_train(Train())
