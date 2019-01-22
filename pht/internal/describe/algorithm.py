from pht.internal import Typed


class AlgorithmRequirement(Typed):
    pass


class FormulaAlgorithmRequirement(AlgorithmRequirement):

    def __init__(self, value: int):
        self._value = value
        if self._value < 1:
            raise ValueError("Minimum value for FormulaAlgorithmRequirement is 1!")

    @property
    def data(self) -> dict:
        return {
            'value': self._value
        }

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'FormulaAlgorithmRequirement'
