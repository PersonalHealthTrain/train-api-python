from typing import Union
from pht.internal.protocol.Copyable import Copyable
from .ModelSummary import ModelSummary


class JsonModelSummary(ModelSummary):
    def __init__(self, val: Union[Copyable, dict, list]):
        self._val = val.copy()

    def copy(self):
        return JsonModelSummary(self._val)

    def __eq__(self, other):
        return (other is self) or (isinstance(other, JsonModelSummary) and self.value == other.value)

    @property
    def type(self) -> str:
        return self.display

    @property
    def display(self) -> str:
        return 'JsonModelSummary'

    @property
    def value(self):
        return self._val
