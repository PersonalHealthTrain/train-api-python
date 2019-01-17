from pht.internal import StationRuntimeInfo, ConjunctionBuilder
from pht.response import RunResponse
from pht.train import SimpleTrain
from pht.requirement import url_by_name, Require
from pht.response.exit_state import SUCCESS
from pht.rebase import DockerRebaseStrategy
from pht.entrypoint import cmd_for_train


class MyTrain(SimpleTrain):
    def __init__(self):
        self.data_source = url_by_name('MY_DATA_SOURCE')

    def requirements(self) -> ConjunctionBuilder:
        return Require(self.data_source)

    def model_summary(self) -> str:
        return 'Hello World'

    def run(self, info: StationRuntimeInfo) -> RunResponse:

        # Execute your algorithm here

        return RunResponse(
            state=SUCCESS,
            free_text_message='Hello world',
            next_train_tag='next_tag',
            rebase=DockerRebaseStrategy(frm='personalhealthtrain/train-api-python:1.0rc1'),
            export_files=[]
        )


if __name__ == '__main__':
    cmd_for_train(MyTrain())
