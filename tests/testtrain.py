from pht.train import Train
from pht.station import StationRuntimeInfo
from pht.response import RunAlgorithmResponse
from pht.response import ListRequirementsResponse
from pht.response import AlgorithmExitState
from pht.response.rebase import DockerRebaseStrategy

class TestTrain(Train):

    def model_summary(self, run_info: StationRuntimeInfo) -> str:
        return 'foo'

    def run_algorithm(self, run_info: StationRuntimeInfo) -> RunAlgorithmResponse:

        # .. Here we do some calculation inside the container
        return RunAlgorithmResponse(
            AlgorithmExitState.SUCCESS,
            'This is a test message',
            'next_station',

        )


    def list_requirements(self, run_info: StationRuntimeInfo) -> ListRequirementsResponse:
        pass
