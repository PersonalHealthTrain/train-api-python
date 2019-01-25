import abc
from pht.internal.train import AbstractTrain
from pht.internal import \
    ConjunctionBuilder,\
    FormulaAlgorithmRequirement,\
    StationRuntimeInfo, \
    TrainDescription


class SimpleTrain(AbstractTrain):

    @abc.abstractmethod
    def requirements(self) -> ConjunctionBuilder:
        pass

    @abc.abstractmethod
    def model_summary(self) -> str:
        pass

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
