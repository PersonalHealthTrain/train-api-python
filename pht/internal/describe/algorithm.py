from pht.internal import Typed


class AlgorithmRequirement(Typed):
    pass


class FormulaAlgorithmRequirement(AlgorithmRequirement):

    def __init__(self, value: dict):
        self._value = value.copy()

    @property
    def data(self) -> dict:
        return self._value

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'FormulaAlgorithmRequirement'
