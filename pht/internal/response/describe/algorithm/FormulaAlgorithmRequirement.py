from collections.abc import Hashable
from pht.internal.util import require
from .AlgorithmRequirement import AlgorithmRequirement


class FormulaAlgorithmRequirement(AlgorithmRequirement, Hashable):

    def __init__(self, formula_id: int):
        self._formula_id = formula_id
        require.type_is_int(self._formula_id)
        require.that(self._formula_id > 0, error_if_not="Minimum value for FormulaAlgorithmRequirement is 1!")

    @property
    def data(self) -> dict:
        return {
            'formula_id': self._formula_id
        }

    def __hash__(self):
        return hash(self._formula_id)

    def copy(self):
        return FormulaAlgorithmRequirement(self._formula_id)
