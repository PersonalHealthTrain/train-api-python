from pht.train import SimpleDockerTrain
from pht.train.component import ConjunctionBuilder, StationRuntimeInfo
from pht.requirement import Require
from pht.requirement.environment_variable import url_by_name
from pht.entrypoint import cli_for_train


class MyTrain(SimpleDockerTrain):
    def __init__(self):
        super().__init__('hello-world', '1.0', 'rebase', ['next-tag'])
        self.data_source = url_by_name('MY_DATA_SOURCE')
        self.output = self.model_file('output')

    def requirements(self) -> ConjunctionBuilder:
        return Require(self.data_source)

    def model_summary(self) -> str:
        return self.output.read_or_default('Not executed yet')

    def run_algorithm(self, info: StationRuntimeInfo, log):
        raise ValueError("Fail: Hello World")


if __name__ == '__main__':
    cli_for_train(MyTrain())
