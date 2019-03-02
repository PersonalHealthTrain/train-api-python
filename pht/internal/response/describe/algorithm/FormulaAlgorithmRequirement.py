from pht.internal.util import require
from .AlgorithmRequirement import AlgorithmRequirement


class FormulaAlgorithmRequirement(AlgorithmRequirement):

    def __init__(self, formula_id: int):
        self._formula_id = formula_id
        require.type_is_int(self._formula_id)
        require.for_value(self._formula_id, lambda x: x > 0, "Minimum value for FormulaAlgorithmRequirement is 1!")

    @property
    def data(self) -> dict:
        return {
            'formula_id': self._formula_id
        }

    @property
    def type(self) -> str:
        return self.type_name

    @property
    def type_name(self) -> str:
        return 'FormulaAlgorithmRequirement'

    def __eq__(self, other):
        return other is self or \
               (isinstance(other, FormulaAlgorithmRequirement) and self._formula_id == other._formula_id)

    def __hash__(self):
        return hash(self._formula_id)

    def copy(self):
        return FormulaAlgorithmRequirement(self._formula_id)
