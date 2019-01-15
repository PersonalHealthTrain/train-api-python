import abc
from pht.internal import AbstractTrain, ConjunctionBuilder, TrainDescription, FormulaAlgorithmRequirement


class SimpleTrain(AbstractTrain):

    @abc.abstractmethod
    def requirements(self) -> ConjunctionBuilder:
        pass

    @abc.abstractmethod
    def model_summary(self) -> str:
        pass

    def describe(self) -> TrainDescription:

        requirements = self.requirements()
        properties = requirements.props
        formulas = [requirements.cnf()]

        return TrainDescription(
            properties=properties,
            formulas=formulas,
            model_summary=self.model_summary(),
            algorithm_requirement=FormulaAlgorithmRequirement({'value': 1}))
