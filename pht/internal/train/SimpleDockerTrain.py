import abc
from typing import List
from pht.internal.train.AbstractTrain import AbstractTrain
from pht.internal.train.StationRuntimeInfo import StationRuntimeInfo
from pht.internal.train.Log import Log
from pht.internal.response.run.RunResponse import RunResponse
from pht.internal.response.run.rebase.RebaseStrategy import DockerRebaseStrategy
from pht.internal.response.run.exit.RunExit import AlgorithmFailure
from pht.internal.response.describe.TrainDescription import TrainDescription
from pht.internal.response.describe.requirement.builder import ConjunctionBuilder
from pht.internal.response.describe.algorithm.FormulaAlgorithmRequirement import FormulaAlgorithmRequirement


class SimpleDockerTrain(AbstractTrain):
    """
    Train class that can be extended if the train completely relies on Docker images.
    In particular, this Train will always use the DockerRebaseStrategy
    """
    def __init__(self, train_name: str, train_version: str, default_rebase_from: str, default_next_train_tags: List[str]):
        super().__init__()
        self.train_name = train_name
        self.train_version = train_version
        self.default_rebase_from = default_rebase_from
        self.default_next_train_tags = default_next_train_tags.copy()

    @abc.abstractmethod
    def requirements(self) -> ConjunctionBuilder:
        pass

    @abc.abstractmethod
    def model_summary(self) -> str:
        pass

    @abc.abstractmethod
    def run_algorithm(self, info: StationRuntimeInfo, log):
        pass

    def run(self, info: StationRuntimeInfo) -> RunResponse:
        log = Log()
        try:
            self.run_algorithm(info, log)
            exit_state = log.exit_state.copy()
        except Exception as e:
            exit_state = AlgorithmFailure(str(e))
        message = log.free_text_message
        rebase_from = log.rebase_from if log.rebase_from is not None else self.default_rebase_from
        next_train_tags = log.next_train_tags if log.next_train_tags is not None else self.default_next_train_tags

        return RunResponse(exit_state, message, DockerRebaseStrategy(
            frm=rebase_from,
            next_train_tags=next_train_tags,
            export_files=self.export_files()
        ))

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
            train_name=self.train_name,
            train_version=self.train_version,
            properties=properties,
            formulas=formulas,
            model_summary=self.model_summary(),
            algorithm_requirement=alg_req)
