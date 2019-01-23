import os
from pht.internal import StationRuntimeInfo, ConjunctionBuilder
from pht.train.response import RunResponse
from pht.train import SimpleTrain
from pht.requirement import url_by_name, Require
from pht.train.response.exit_state import SUCCESS
from pht.rebase import DockerRebaseStrategy
from pht.entrypoint import cmd_for_train

model_file = '/opt/model'


class MyTrain(SimpleTrain):
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
    cmd_for_train(MyTrain())
