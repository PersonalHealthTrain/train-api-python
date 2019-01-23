from pht.internal import Typed


class AlgorithmRequirement(Typed):
    pass


class FormulaAlgorithmRequirement(AlgorithmRequirement):

    def __init__(self, value: int):
        self._value = value

        if not isinstance(self._value, int) or isinstance(self._value, bool):
            raise TypeError("Provided value : \'{}\' is not of type int!".format(str(value)))

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

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, FormulaAlgorithmRequirement):
            return False
        return self._value == other._value

    def __hash__(self):
        return hash(self._value)

    def copy(self):
        return FormulaAlgorithmRequirement(self._value)

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memodict=None):
        return self.copy()
