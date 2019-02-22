from pht.internal.util import require

from .ModelSummary import ModelSummary


class StringModelSummary(ModelSummary):
    def __init__(self, val: str):
        self._val = val
        require.type_is_str(self._val)

    def copy(self):
        return StringModelSummary(self._val)

    def __eq__(self, other):
        return (other is self) or (isinstance(other, StringModelSummary) and self.value == other.value)

    def __hash__(self):
        return hash(self._val)

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'StringModelSummary'

    @property
    def value(self):
        return self._val
