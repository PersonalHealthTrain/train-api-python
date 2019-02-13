import os
from pht.internal import StationRuntimeInfo, ConjunctionBuilder
from pht.train.entity import RunResponse
from pht.train import SimpleTrain
from pht.requirement2 import url_by_name, Require
from pht.internal.run.exit.RunExit import SUCCESS
from pht.internal.run.rebase import DockerRebaseStrategy
from pht.internal.entrypoint import cli_for_train

model_file = '/opt/model'


class MyTrain(SimpleTrain):
    def __init__(self):
        self.data_source = url_by_name('MY_DATA_SOURCE')

    # Define the requirements of the Train here
    def requirements(self) -> ConjunctionBuilder:
        return Require(self.data_source)

    # Generate the Summary of the Model
    def model_summary(self) -> str:
        return 'Hello from: DeepMedic'

    # Run the algorithm (fetch data, generate model, etc.)
    def run(self, info: StationRuntimeInfo) -> RunResponse:

        # Fetch the data here

        # Implement the algorithm here and serialze the learned model to the filesystem, something like this
        if not os.path.exists('/opt'):
            os.mkdir('/opt')
        with open(model_file, 'w') as f:
            f.write('Hello World')

        return RunResponse(
            run_exit=SUCCESS,
            free_text_message='Hello world',
            rebase=DockerRebaseStrategy(
                frm='personalhealthtrain/train-api-python:1.0rc3',
                next_train_tags='station.2',
                export_files=[model_file]
            )
        )


if __name__ == '__main__':
    cli_for_train(MyTrain())
