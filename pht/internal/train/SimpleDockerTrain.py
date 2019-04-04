"""
Base Class for Trains that are based on Docker Images
"""
from abc import abstractmethod
from typing import List, Union, Optional
from pht.internal.train.AbstractTrain import AbstractTrain
from pht.internal.train.StationRuntimeInfo import StationRuntimeInfo
from pht.internal.response.run.RunResponse import RunResponse
from pht.internal.response.run.rebase.RebaseStrategy import DockerRebaseStrategy
from pht.internal.response.run.exit.RunExit import AlgorithmFailureRunExit
from pht.internal.response.describe.TrainDescription import TrainDescription
from pht.internal.response.describe.requirement.builder import ConjunctionBuilder
from pht.internal.response.describe.algorithm.FormulaAlgorithmRequirement import FormulaAlgorithmRequirement
from pht.internal.response.run.exit.RunExit import AlgorithmSuccessRunExit, RunExit


class Log:
    """
    Log file that the train can write to while running the algorithm to determine the Train Responses
    """
    def __init__(self):
        self.exit_state = AlgorithmSuccessRunExit('')
        self.free_text_message = ''
        self.rebase_from = None
        self.next_train_tags = None

    def set_exit_state(self, exit_state: RunExit):
        self.exit_state = exit_state

    def set_free_text_message(self, m: str):
        self.free_text_message = m

    def set_rebase_from(self, frm: str):
        self.rebase_from = frm

    def set_next_train_tags(self, tags: List[str]):
        self.next_train_tags = tags.copy()


class SimpleDockerTrain(AbstractTrain):
    """
    Train class that can be extended if the train completely relies on Docker images.
    In particular, this Train will always use the DockerRebaseStrategy
    """
    def __init__(self,
                 train_name: str,
                 train_version: str,
                 default_rebase_from: str,
                 default_next_train_tags: List[str]):
        super().__init__()
        self.train_name = train_name
        self.train_version = train_version
        self.default_rebase_from = default_rebase_from
        self.default_next_train_tags = default_next_train_tags.copy()

    @abstractmethod
    def requirements(self) -> Optional[ConjunctionBuilder]:
        """
        The Conjunction expression to define the algorithm requirements of the train, or None if no such requirements
        exists
        """
        pass

    @abstractmethod
    def model_summary(self) -> Union[str, dict, list]:
        pass

    @abstractmethod
    def run_algorithm(self, info: StationRuntimeInfo, log):
        pass

    def run(self, info: StationRuntimeInfo) -> RunResponse:
        log = Log()
        try:
            self.run_algorithm(info, log)
            exit_state = log.exit_state.deepcopy()
        except Exception as e:
            exit_state = AlgorithmFailureRunExit(str(e))
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
