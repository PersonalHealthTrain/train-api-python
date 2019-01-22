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
        properties = requirements.props
        formulas = [requirements.cnf()]

        return TrainDescription(
            properties=properties,
            formulas=formulas,
            model_summary=self.model_summary(),
            algorithm_requirement=FormulaAlgorithmRequirement(1))
