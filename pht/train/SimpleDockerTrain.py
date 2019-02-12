import abc
from typing import List
from pht.internal.train import AbstractTrain
from pht.train.response import RunResponse
from pht.rebase import DockerRebaseStrategy
from pht.train.response.RunExit import AlgorithmFailure, AlgorithmSuccess, RunExit
from pht.internal import \
    ConjunctionBuilder,\
    FormulaAlgorithmRequirement,\
    StationRuntimeInfo, \
    TrainDescription


class Log:
    def __init__(self):
        self.exit_state = AlgorithmSuccess('')
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

    @abc.abstractmethod
    def requirements(self) -> ConjunctionBuilder:
        pass

    @abc.abstractmethod
    def model_summary(self) -> str:
        pass

    @abc.abstractmethod
    def default_rebase_from(self) -> str:
        pass

    @abc.abstractmethod
    def default_next_train_tags(self) -> List[str]:
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
        rebase_from = log.rebase_from if log.rebase_from is not None else self.default_rebase_from()
        next_train_tags = log.next_train_tags if log.next_train_tags is not None else self.default_next_train_tags()
        export_files = self.list_existing_trainfiles()

        return RunResponse(exit_state, message, DockerRebaseStrategy(
            frm=rebase_from,
            next_train_tags=next_train_tags,
            export_files=export_files
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
            properties=properties,
            formulas=formulas,
            model_summary=self.model_summary(),
            algorithm_requirement=alg_req)
