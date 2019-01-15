from pht.train import SimpleTrain
from pht.internal.station import StationRuntimeInfo
from pht.internal.response import RunAlgorithmResponse
from pht.internal.response import ListRequirementsResponse
from pht.internal.response import AlgorithmExitState
from pht.internal.rebase import DockerRebaseStrategy


class TestTrain(SimpleTrain):

    def model_summary(self, run_info: StationRuntimeInfo) -> str:
        return 'foo'

    def run_algorithm(self, run_info: StationRuntimeInfo) -> RunAlgorithmResponse:

        # .. Here we do some calculation inside the container
        return RunAlgorithmResponse(
            AlgorithmExitState.SUCCESS,
            'This is a test message',
            'next_station',
            DockerRebaseStrategy('personalhealthtrain/image:tag'),
            export_files=[]
        )


    def list_requirements(self, run_info: StationRuntimeInfo) -> ListRequirementsResponse:
        pass
