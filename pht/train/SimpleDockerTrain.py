import abc
from pht.internal.train import TrainCommandInterface, RunResponse
from pht.train.response.exit_state import AlgorithmExitState
from pht.internal import \
    ConjunctionBuilder,\
    FormulaAlgorithmRequirement,\
    StationRuntimeInfo, \
    TrainDescription


class SimpleDockerTrain(TrainCommandInterface):

    @abc.abstractmethod
    def requirements(self) -> ConjunctionBuilder:
        pass

    @abc.abstractmethod
    def model_summary(self) -> str:
        pass

    @abc.abstractmethod
    def run_algorithm(self, info: StationRuntimeInfo) -> AlgorithmExitState:
        pass

    def run(self, info):
        # TODO Implement Me
        exit_state = self.run_algorithm(info)
        return RunResponse(exit_state, )


    def describe(self, info: StationRuntimeInfo) -> TrainDescription:

        requirements = self.requirements()
        if requirements is not None:
            properties = requirements.props
            formulas = [requirements.cnf()]
            alg_req = FormulaAlgorithmRequirement(1)
        else:
            properties = {}
            formulas = []
            alg_req = None

        return TrainDescription(
            properties=properties,
            formulas=formulas,
            model_summary=self.model_summary(),
            algorithm_requirement=alg_req)
